from flask import Flask, request, jsonify
import asyncio
import os
from dotenv import load_dotenv

from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

load_dotenv()

EMAIL = os.getenv('EMAIL')
PSW = os.getenv('PASSWORD')
 
app = Flask(__name__)

async def toggleSwitch(plugName: str) -> str:
    http_api_client = await MerossHttpClient.async_from_user_password(api_base_url='https://iotx-eu.meross.com',email=EMAIL, password=PSW)

    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Retrieve all the MSS310 devices that are registered on this account
    await manager.async_device_discovery()
    plugs = manager.find_devices(device_name=plugName)

    if len(plugs) < 1:
        print("No MSS310 plugs found...")
        
        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()

        return jsonify("No plugs")
    else:
        print(plugs[0].name)
        await plugs[0].async_update()
        await plugs[0].async_toggle(channel=0)

        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()

        print('All done!')
        return jsonify("Done")


@app.route("/")
def home():
    return jsonify("Meross API is running"), 200

@app.route("/toggle/<plugName>")
def toggle(plugName):
    asyncio.run(toggleSwitch(plugName))
    return jsonify("Toggled"), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
