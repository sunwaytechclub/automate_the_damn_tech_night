import Cookie from "js-cookie";
import Network from "./network";
export default {
	/**
	 * @param  {string} username
	 * @param  {string} password
	 * @returns {string} Token
	 */
	async login({ username, password }) {
		let jwt = await Network.post({
			path: "/auth/",
			body: {
				username,
				password,
			},
		});
		return jwt["token"];
	},
	/**
	 * @param  {String} token
	 */
	storeTokenInCookie({ token }) {
		Cookie.set("token", token);
	},
	logout() {
		Cookie.remove("token");
	},
};
