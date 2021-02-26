import Network from "./network";
export default {
	/**
	 * @returns {Speaker[]} n - An array of speakers
	 */
	async getAllSpeakers() {
		let speakers = await Network.authGet({
			path: "/api/v1/speaker/",
		});
		return speakers;
	},
	/**
	 * @param  {number} id - The ID of the speaker
	 * @returns {Speaker} n - The speaker details
	 */
	async getSpeaker({ id }) {
		let speaker = await Network.authGet({
			path: `/api/v1/speaker/${id}/`,
		});
		return speaker;
	},
	/**
	 * @param  {string} name - The name of the speaker
	 * @param  {string} position - Experiences and positions the speaker have
	 * @param  {file} avatar - An input tag image file
	 * @returns {Speaker} n - The created speaker profile
	 */
	async createSpeaker({ name, position, avatar }) {
		let formData = new FormData();
		formData.append("name", name);
		formData.append("position", position);
		formData.append("avatar", avatar);

		let speaker = await Network.authPostWithFormData({
			path: "/api/v1/speaker/",
			formData,
		});
		return speaker;
	},
	/**
	 * @param  {number} id
	 * @param  {string=} name
	 * @param  {string=} position
	 * @param  {file=} avatar
	 * @returns {Speaker} n - The updated speaker profile
	 */
	async updateSpeaker({ id, name = null, position = null, avatar = null }) {
		let formData = new FormData();
		formData.append("name", name);
		formData.append("position", position);
		formData.append("avatar", avatar);

		let speaker = await Network.authPatchWithFormData({
			path: `/api/v1/speaker/${id}/`,
			formData,
		});
		return speaker;
	},
	/**
	 * @param  {number} id - ID of the speaker
	 */
	async deleteSpeaker({ id }) {
		let speaker = await Network.authDelete({
			path: `/api/v1/speaker/${id}/`,
		});
		return speaker;
	},
};
