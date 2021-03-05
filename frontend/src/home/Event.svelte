<script>
	import Header from "@/components/Header.svelte";
	import ActionButton from "@/components/ActionButton.svelte";
	import getLastSegUrl from "@/utils/getLastSegUrl.js";
	import { onMount } from "svelte";

	import EventAPI from "@/services/event.js";
	import pushState from "@/utils/pushState";

	const eventId = getLastSegUrl();

	let event = {};
	let writeupContainer;
	let content;
	let copyText = "Copy";
	let topics = []

	onMount(async () => {
		const data = await EventAPI.getEvent({
			id: eventId,
		});

		event = data;
		topics = data.topic
		content = event.writeup;
		event.writeup = event.writeup.replace(/\n/g, "<br />");
		writeupContainer.innerHTML = event.writeup;
	});

	function copyWriteup() {
		const textarea = document.createElement("textarea");
		textarea.value = content;
		document.body.appendChild(textarea);
		textarea.select();
		document.execCommand("copy");
		copyText = "Copied";
		document.body.removeChild(textarea);
	}

	async function downloadImage(url, fileName) {
		const response = await fetch(url);
		const object = await response.blob();
		const objectURL = URL.createObjectURL(object);
		const link = document.createElement("a");
		link.href = objectURL;
		link.setAttribute("download", `tech-night-poster-${fileName}.jpg`);
		link.setAttribute("style", "display: none");
		document.body.appendChild(link);
		link.click();
	}
	
	async function downloadAllPoster() {
		await downloadPoster()
		for (let i = 0; i < event.topic.length; i++) {
			await downloadTopicPoster(i)
		}
	}

	function downloadPoster() {
		downloadImage(event.poster, `#${event.episode}`)
	}

	function downloadTopicPoster(index) {
		downloadImage(event.topic[index].poster, event.topic[index].speaker.name)
	}

	function navigateEditEvent() {
		pushState(`/home/event/edit/${event.id}`)
	}
</script>

<div class="wrapper">
	<div class="content">
		{#await event}
			<!-- TODO: loader -->
		{:then}
			<Header title="Tech Night #{event.episode}" previousPath="/home" />
			<div class="page-subheader">
				<p class="subheader-text"></p>
				<ActionButton
					label="Edit"
					iconPath="/assets/icons/edit-purple.svg"
					textColor="var(--purple-2)"
					on:click={navigateEditEvent}
				/>
			</div>
			<div class="generated-content-wrapper">
				<div class="generated-content">
					<div class="generated-writeup line">
						<div class="field-title">
							<p class="field-title-text">Generated Writeup</p>
							<ActionButton
								label={copyText}
								iconPath="/assets/icons/copy.svg"
								textColor="var(--dark-blue)"
								on:click={copyWriteup}
							/>
						</div>
						<div class="content-writeup" bind:this={writeupContainer} />
					</div>
					<div class="generated-poster line">
						<div class="field-title">
							<p class="field-title-text">Generated Poster</p>
							<ActionButton
								label="Download All"
								iconPath="/assets/icons/download.svg"
								textColor="var(--dark-blue)"
								on:click={downloadAllPoster}
							/>
						</div>
						<div class="poster-div">
							<span class="poster-wrapper">
							<img src={event.poster} alt="" class="poster" />
							<div class="download-icon-wrapper" on:click={downloadPoster}>
								<img src="/assets/icons/download.svg" alt="download" class="download-poster" />
							</div>
						</span>
							{#each topics as topic, i}
								<span class="poster-wrapper">
									<img src={topic.poster} alt="" class="poster"/>
									<div class="download-icon-wrapper" on:click={() => {downloadTopicPoster(i)}}>
										<img src="/assets/icons/download.svg" alt="download" class="download-poster" />
									</div>
								</span>
							{/each}
						</div>
					</div>
				</div>
			</div>
		{/await}
	</div>
</div>

<style>
	.wrapper {
		width: 98%;
		display: flex;
	}
	.content {
		margin-top: 20px;
		display: flex;
		flex-direction: column;
		width: 100%;
	}
	.page-subheader {
		display: flex;
		align-items: center;
		justify-content: space-between;
		border-bottom: 2px var(--light-grey) solid;
		margin-bottom: 20px;
		padding-bottom: 10px;
		width: 95%;
	}
	.subheader-text {
		font: var(--primary-font-regular);
		font-size: 10px;
		color: var(--dark-blue);
	}
	.generated-content-wrapper {
		display: flex;
		justify-content: center;
	}
	.generated-content {
		width: 50vw
	}
	.generated-writeup {
		width: 95%;
	}
	.generated-poster {
		width: 95%;
	}
	.field-title {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 10px;
	}
	.field-title-text {
		font: var(--primary-font-semibold);
	}
	.content-writeup {
		background-color: var(--light-grey);
		padding: 30px;
		width: 100%;
	}
	.poster-wrapper {
		width: 50%;
		height: 100%;
		display: flex;
		position: relative;
	}
	.poster-div {
		display: flex;
		flex-wrap: wrap;
	}
	.poster {
		width: 95%;
		margin-bottom: 20px;
		cursor: pointer;
		background-color: black;
		margin-right: 10px;
	}
	.download-icon-wrapper {
		position: absolute;
		left: 0;
		top: 0;
		width: 95%;
		height: 95%;
		display: grid;
		place-items: center;
		visibility: hidden;
	}
	.poster:hover ~ .download-icon-wrapper {
		visibility: visible;
		background-color: rgba(255, 255, 255, 0.9);
		cursor: pointer;
	}
	.download-icon-wrapper:hover {
		visibility: visible;
		background-color: rgba(255, 255, 255, 0.9);
		cursor: pointer;
	}
	.download-poster {
		width: 40px;
	}
	.line {
		padding-bottom: 20px;
		border-bottom: 2px var(--light-grey) solid;
		margin-bottom: 30px;
	}
	@media only screen and (max-width: 966px) {
		.generated-content {
			width: 80vw;
			margin-left: 10px;
		}
		.poster-wrapper {
			width: 100%;
		}
		.poster {
			width: 100%
		}
	}
</style>
