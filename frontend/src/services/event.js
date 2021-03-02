import Network from "./network";
export default {
	/**
	 * @returns All the events
	 */
	async getAllEvents() {
		let events = await Network.authGet({
			path: "/api/v1/event/",
		});
		return events;
	},
	/**
	 * @param  {number} id
	 * @returns {Event} - n
	 */
	async getEvent({ id }) {
		let event = await Network.authGet({
			path: `/api/v1/event/${id}/`,
		});
		return event;
	},
	/**
	 * @param  {number} episode
	 * @param  {Date} datetime
	 * @param  {Topic[]} topic - An array of all the topic related
	 * @returns {Event} n
	 */
	async createEvent({ episode, datetime, topic }) {
		let event = await Network.authPost({
			path: "/api/v1/event/",
			body: {
				episode,
				datetime: datetime.toISOString(),
				topic,
			},
		});
		return event;
	},
	/**
	 * @param  {number} id
	 * @param  {number=} episode
	 * @param  {Date=} datetime
	 * @param  {Topic[]=} topic
	 * @returns {Event} n
	 */
	async updateEvent({ id, episode = null, datetime = null, topic = null }) {
		let body = { episode, datetime, topic };
		Object.keys(body).map((key) => !body[key] && delete body[key]);
		let event = await Network.authPatch({
			path: `/api/v1/event/${id}/`,
			body,
		});
		return event;
	},
	/**
	 * @param  {number} id
	 */
	async deleteEvent({ id }) {
		let event = await Network.authDelete({
			path: `/api/v1/event/${id}/`,
		});
		return event;
	},
};
