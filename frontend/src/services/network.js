import { Domain } from "@/config/index";
import Cookie from "js-cookie";
export default {
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @returns {Object} response
	 */
	async get({ path = null, url = null }) {
		url = url || Domain + path;
		let response = await fetch(url);
		let data = await response.json();
		return data;
	},
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @param  {Object} body
	 * @returns {Object} response
	 */
	async post({ path = null, url = null, body }) {
		url = url || Domain + path;
		let response = await fetch(url, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(body),
		});
		let data = await response.json();
		return data;
	},
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @returns {Object} response
	 */
	async authGet({ path = null, url = null }) {
		url = url || Domain + path;
		let response = await fetch(url, {
			headers: {
				Authorization: `Token ${Cookie.get("token")}`,
			},
		});
		let data = await response.json();
		return data;
	},
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @param  {Object} body
	 * @returns {Object} response
	 */
	async authPost({ path = null, url = null, body }) {
		url = url || Domain + path;
		let response = await fetch(url, {
			method: "POST",
			headers: {
				Authorization: `Token ${Cookie.get("token")}`,
				"Content-Type": "application/json",
			},
			body: JSON.stringify(body),
		});
		let data = await response.json();
		return data;
	},
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @param  {FormData} formData
	 * @returns {Object} response
	 */
	async authPostWithFormData({ path = null, url = null, formData }) {
		url = url || Domain + path;
		let response = await fetch(url, {
			method: "POST",
			headers: {
				Authorization: `Token ${Cookie.get("token")}`,
			},
			body: formData,
		});
		let data = await response.json();
		return data;
	},
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @param  {Object} body
	 * @returns {Object} response
	 */
	async authPatch({ path = null, url = null, body }) {
		url = url || Domain + path;
		let response = await fetch(url, {
			method: "PATCH",
			headers: {
				Authorization: `Token ${Cookie.get("token")}`,
				"Content-Type": "application/json",
			},
			body: JSON.stringify(body),
		});
		let data = await response.json();
		return data;
	},
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @param  {FormData} formData
	 * @returns {Object} response
	 */
	async authPatchWithFormData({ path = null, url = null, formData }) {
		url = url || Domain + path;
		let response = await fetch(url, {
			method: "PATCH",
			headers: {
				Authorization: `Token ${Cookie.get("token")}`,
			},
			body: formData,
		});
		let data = await response.json();
		return data;
	},
	/**
	 * @param  {string=} path
	 * @param  {string=} url
	 * @returns {string} response
	 */
	async authDelete({ path = null, url = null }) {
		url = url || Domain + path;
		let response = await fetch(url, {
			method: "DELETE",
			headers: {
				Authorization: `Token ${Cookie.get("token")}`,
			},
		});
		let data = await response.text();
		return data;
	},
};
