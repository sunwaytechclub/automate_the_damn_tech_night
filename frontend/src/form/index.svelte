<script>
	import TextInput from "@/components/TextInput.svelte";
	import ActionButton from "@/components/ActionButton.svelte";
	import CheckBox from "@/components/CheckBox.svelte";
	import Button from "@/components/Button.svelte";
	import DatePicker from "@/components/DatePicker.svelte";
	import TimePicker from "@/components/TimePicker.svelte";
	import SideNavbar from "@/components/SideNavbar.svelte";
	import Speaker from "@/form/Speaker.svelte";

	import { storeFE, idIncrement } from "@/components/stores.js";

	let speakers = [
		{ value: "rain", label: "Rain Chai" },
		{ value: "nick", label: "Nick" },
		{ value: "yong", label: "Yong" },
		{ value: "lynus", label: "Lynus" },
		{ value: "eason", label: "Eason" },
	];

	$storeFE = [
		{ id: 1, topic: "First option", caption: "additional note", speakers },
		// other items can go here
	];

	idIncrement.set(2); // this is a crude way to increment the id for new items

	let isPostFacebook = true;
	let isPostTelegram = true;
	let isSendDepartments = false;

	let episode;
	let date;
	let time;
	let venue;
	let registrationLink;

	let episodeError = {};
	let dateError = {};
	let timeError = {};
	let venueError = {};
	let registrationLinkError = {};

	function addSpeaker() {
		var l = $storeFE.length; // get our current items list count
		$storeFE[l] = {
			id: $idIncrement,
			topic: "Another option",
			caption: "additional note",
			speakers,
		};
		console.log($storeFE);
		$idIncrement++; // increment our id to add additional items
	}

	function publish() {
		let episodeValue = episode.value;
		let dateValue = date;
		let timeValue = time;
		let venueValue = venue.value;
		let registrationLinkValue = registrationLink.value;

		if (episodeValue == "") {
			episodeError.enabled = true;
			episodeError.message = "Please fill in episode number";
		} else {
			episodeError.enabled = false;
		}

		if (dateValue == null) {
			dateError.enabled = true;
			dateError.message = "Please select a date";
		} else {
			dateError.enabled = false;
		}

		if (timeValue == null) {
			timeError.enabled = true;
			timeError.message = "Please select a time";
		} else {
			timeError.enabled = false;
		}

		if (venueValue == "") {
			venueError.enabled = true;
			venueError.message = "Please fill in venue or platform";
		} else {
			venueError.enabled = false;
		}

		if (registrationLinkValue == "") {
			registrationLinkError.enabled = true;
			registrationLinkError.message = "Please fill in registration link";
		} else {
			registrationLinkError.enabled = false;
		}
	}
</script>

<div class="wrapper">
	<div class="content">
		<p class="page-header">New Tech Night Event</p>
		<div>
			<TextInput
				bind:value={episode}
				label="Tech Night Episode"
				placeholder="Tech Night Episode"
				error={episodeError}
			/>
		</div>
		<div>
			{#each $storeFE as item}
				<svelte:component this={Speaker} objAttributes={item} />
			{/each}
			<div class="add-topic-div">
				<ActionButton on:click={addSpeaker} />
			</div>
		</div>
		<div class="side-by-side">
			<DatePicker bind:date error={dateError} />
			<TimePicker bind:time error={timeError} />
		</div>
		<div class="side-by-side" style="margin-bottom: 20px">
			<TextInput
				bind:value={venue}
				label="Venue / Platform"
				placeholder="Venue / Platform"
				error={venueError}
			/>
			<TextInput
				bind:value={registrationLink}
				label="Registration Link"
				placeholder="Registration Link"
				error={registrationLinkError}
			/>
		</div>
		<CheckBox label="Post on Facebook Group" bind:checked={isPostFacebook} />
		<CheckBox label="Post on Telegram " bind:checked={isPostTelegram} />
		<CheckBox
			label="Send emails to departments"
			subText="Email will be sent to SET, A-Level, SFP, AUSMAT, DIIT. To edit, go to admin portal."
			bind:checked={isSendDepartments}
		/>
		<div class="publish-button-div">
			<Button style="width: 50%" label="PUBLISH" on:click={publish} />
		</div>
	</div>
</div>

<style>
	.wrapper {
		width: 100%;
		display: flex;
	}
	.content {
		margin-top: 20px;
		width: 50%;
	}
	.page-header {
		font: var(--primary-font-bold);
		font-size: 35px;
		margin-bottom: 30px;
	}
	.side-by-side {
		display: grid;
		grid-template-columns: auto auto;
		column-gap: 30px;
	}
	.add-topic-div {
		border-bottom: 2px var(--light-grey) solid;
		padding-bottom: 15px;
		margin-top: 10px;
		margin-bottom: 20px;
	}
	.publish-button-div {
		width: 100%;
		display: flex;
		justify-content: center;
		margin: 40px 0;
	}
</style>
