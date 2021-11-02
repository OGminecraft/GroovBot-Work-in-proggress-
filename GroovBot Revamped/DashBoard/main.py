from quart import Quart, render_template, request, session, redirect, url_for
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc

app = Quart(__name__)
ipc_client = ipc.Client(secret_key = "what ever you want just no spaces")

app.config["SECRET_KEY"] = "what ever password u want"
app.config["DISCORD_CLIENT_ID"] = 1234567891011121314151617181920  #your client id here
app.config["DISCORD_CLIENT_SECRET"] = "your client serceret here"
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)

@app.route("/")
async def home():
	guild_count = await ipc_client.request("get_guild_count")
	return await render_template("index.html", guild_number = guild_count, authorized = await discord.authorized)

@app.route("/login")
async def login():
	return await discord.create_session()

@app.route("/callback")
async def callback():
	try:
		await discord.callback()
	except:
		pass#return redirect(url_for("login"))

	return redirect(url_for("dashboard")) #You should return redirect(url_for("dashboard")) here

@app.route("/dashboard")
async def dashboard():
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild_count = await ipc_client.request("get_guild_count")
	guild_ids = await ipc_client.request("get_guild_ids")

	user_guilds = await discord.fetch_guilds()

	guilds = []

	for guild in user_guilds:
		if guild.permissions.administrator:			
			guild.class_color = "green-border" if guild.id in guild_ids else "red-border"
			guilds.append(guild)

	guilds.sort(key = lambda x: x.class_color == "red-border")
	name = (await discord.fetch_user()).name
	return await render_template("dashboard.html", guild_count = guild_count, guilds = guilds, username=name)

@app.route("/dashboard/<int:guild_id>")
async def dashboard_server(guild_id):
	if not await discord.authorized:
		return redirect(url_for("login")) 

	user = await discord.fetch_user()
	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	if guild is None:
		return redirect(f'https://discord.com/oauth2/authorize?&client_id={app.config["DISCORD_CLIENT_ID"]}&scope=bot&permissions=8&guild_id={guild_id}&response_type=code&redirect_uri={app.config["DISCORD_REDIRECT_URI"]}')
	return await render_template("serverdash.html", guild_name = guild["name"], username = user.name, userid = user.discriminator, guild = guild)

@app.route(f"/dashboard/<int:guild_id>/music")
async def music_cat(guild_id):
	user = await discord.fetch_user()
	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	return await render_template("music.cat.html", username = user.name, userid = user.discriminator, guild_name = guild["name"], guild = guild)

@app.route(f"/dashboard/<int:guild_id>/reaction_roles")
async def rr_cat(guild_id):
	user = await discord.fetch_user()
	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	return await render_template("rr.cat.html", username = user.name, userid = user.discriminator, guild_name = guild["name"], guild = guild)

@app.route(f"/dashboard/<int:guild_id>/fun")
async def fun_cat(guild_id):
	user = await discord.fetch_user()
	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	return await render_template("fun.cat.html", username = user.name, userid = user.discriminator, guild_name = guild["name"], guild = guild)

@app.route(f"/dashboard/<int:guild_id>/other")
async def other_cat(guild_id):
	user = await discord.fetch_user()
	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	return await render_template("other.cat.html", username = user.name, userid = user.discriminator, guild_name = guild["name"], guild = guild)

@app.route(f"/dashboard/<int:guild_id>/settings")
async def settings_cat(guild_id):
	user = await discord.fetch_user()
	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	return await render_template("settings.cat.html", username = user.name, userid = user.discriminator, guild_name = guild["name"], guild = guild, user_avatar = user.avatar_url)

if __name__ == "__main__":
    app.run(debug=True)
