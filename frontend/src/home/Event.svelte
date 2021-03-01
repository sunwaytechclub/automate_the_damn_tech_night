<script>
	import SideNavbar from "@/components/SideNavbar.svelte";
	import Header from "@/components/Header.svelte";
	import ActionButton from "@/components/ActionButton.svelte";
	import getLastSegUrl from "@/utils/getLastSegUrl.js";
	import { onMount } from "svelte";

	import EventAPI from "@/services/event.js";

	let eventId = getLastSegUrl();

	let event = {};
	let writeupContainer;
	let content;
	let copyText = "Copy";

	onMount(async () => {
		let data = await EventAPI.getEvent({
			id: eventId,
		});
		event = data;
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

	async function downloadPoster() {
		const response = await fetch(event.poster);
		const object = await response.blob();
		const objectURL = URL.createObjectURL(object);
		const link = document.createElement("a");
		link.href = objectURL;
		link.setAttribute("download", `tech-night-poster-#${event.episode}.jpg`);
		link.setAttribute("style", "display: none");
		document.body.appendChild(link);
		link.click();
	}
</script>

<div class="wrapper">
	<div class="content">
		{#await event}
			<!-- TODO: loader -->
		{:then}
			<Header title="Tech Night #{event.episode}" previousPath="/home" />
			<div class="page-subheader">
				<!-- <p class="subheader-text">{formattedDate}</p> -->
			</div>
			<div class="generated-content line">
				<div class="field-title">
					<p class="field-title-text">Generated Content</p>
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
						label="Download"
						iconPath="/assets/icons/download.svg"
						textColor="var(--dark-blue)"
						on:click={downloadPoster}
					/>
				</div>
				<img src={event.poster} alt="" class="poster" />
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
	.generated-content {
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
	.poster {
		width: 100%;
	}
	.line {
		padding-bottom: 20px;
		border-bottom: 2px var(--light-grey) solid;
		margin-bottom: 30px;
	}
	@media only screen and (max-width: 600px) {
		.generated-content {
			margin-left: 5px;
		}
	}
</style>
