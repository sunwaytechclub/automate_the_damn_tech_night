<script>
	import TextInput from "@/components/TextInput.svelte";
	import ActionButton from "@/components/ActionButton.svelte";
	import Button from "@/components/Button.svelte";
	import DatePicker from "@/components/DatePicker.svelte";
	import TimePicker from "@/components/TimePicker.svelte";
	import Header from "@/components/Header.svelte";
	import SpeakerField from "@/home/components/SpeakerField.svelte";

	import Event from "@/services/event.js";

	import { storeFE, idIncrement } from "@/components/stores.js";

	import Speaker from "@/services/speaker.js";
	import { onMount } from "svelte";
	import pushState from "@/utils/pushState";

	let speakers = [];

	onMount(async () => {
		let data = await Speaker.getAllSpeakers();

		for (let i = 0; i < data.length; i++) {
			let speaker = {
				label: data[i].name,
				value: data[i].id,
			};
			speakers.push(speaker);
		}
		$storeFE = [{ id: 1, topic: "", hook: "", why: "", what: "", speakers }];
	});

	$storeFE = [];

	idIncrement.set(2); // this is a crude way to increment the id for new items

	// let isPostFacebook = true;
	// let isPostTelegram = true;
	// let isSendDepartments = false;

	let episode;
	let date;
	let time;

	let episodeError = {};
	let dateError = {};
	let timeError = {};
	let topicError = {}

	function addSpeaker() {
		var l = $storeFE.length; // get our current items list count
		$storeFE[l] = { id: $idIncrement, topic: "", caption: "", speakers };
		console.log($storeFE);
		$idIncrement++; // increment our id to add additional items
	}

	async function publish() {
		let episodeValue = episode.value;
		let dateValue = date;
		let timeValue = time;

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
			return timeError.message = "Please select a time";
		} else {
			timeError.enabled = false;
		}
		
		let hours = timeValue.getHours();
		let minutes = timeValue.getMinutes();

		let day = dateValue.getDate();
		let month = dateValue.getMonth();
		let year = dateValue.getFullYear();
		
		let datetime = new Date(year, month, day, hours, minutes);

		let topics = [];

		for (let i = 0; i < $storeFE.length; i++) {

			if ($storeFE[i].selectedSpeaker == undefined || $storeFE[i].topic.value == "" || $storeFE[i].hook.value == "" ||
				$storeFE[i].why.value == "" || $storeFE[i].what.value == "") {
					topicError.message = "Please fill in all the topic fields"
					return topicError.enabled = true
			}

			let topic = {
				speaker: $storeFE[i].selectedSpeaker,
				title: $storeFE[i].topic.value,
				hook: $storeFE[i].hook.value,
				why: $storeFE[i].why.value,
				what: $storeFE[i].what.value,
			};
			topics.push(topic);
		}


		let response = await Event.createEvent({
			episode: parseInt(episodeValue, 10),
			datetime,
			topic: topics,
		});
		pushState("/home");
	}
</script>

<div class="wrapper">
	<div class="content">
		<Header title="Create Event" previousPath="/home" />
		<div class="page-subheader">
			<p class="subheader-text">Create a tech night event</p>
		</div>
		{#await speakers}
			<!-- TODO: loader -->
		{:then}
			<div class="form">
				<div>
					<TextInput
						bind:instance={episode}
						label="Tech Night Episode"
						placeholder="Tech Night Episode"
						error={episodeError}
						type="number"
					/>
				</div>
				<div>
					{#each $storeFE as item}
						<svelte:component this={SpeakerField} objAttributes={item} />
					{/each}
					<div class="add-topic-div">
						<ActionButton on:click={addSpeaker} />
					</div>
					{#if topicError.enabled}
						<p class="error-message">{topicError.message}</p>
					{/if}
				</div>
				<div class="side-by-side">
					<DatePicker bind:date error={dateError} />
					<TimePicker bind:time error={timeError} />
				</div>
				<!-- <div class="side-by-side" style="margin-bottom: 20px">
					<TextInput
						bind:instance={venue}
						label="Venue / Platform"
						placeholder="Venue / Platform"
						error={venueError}
					/>
					<TextInput
						bind:instance={registrationLink}
						label="Registration Link"
						placeholder="Registration Link"
						error={registrationLinkError}
					/>
				</div> -->
				<!-- <CheckBox label="Post on Facebook Group" bind:checked={isPostFacebook}/>
            <CheckBox label="Post on Telegram " bind:checked={isPostTelegram}/>
            <CheckBox label="Send emails to departments" 
                subText="Email will be sent to SET, A-Level, SFP, AUSMAT, DIIT. To edit, go to admin portal."
                bind:checked={isSendDepartments}/> -->
				<div class="publish-button-div">
					<Button style="width: 50%" label="PUBLISH" on:click={publish} />
				</div>
			</div>
		{/await}
	</div>
</div>

<style>
	.wrapper {
		width: 100%;
		display: flex;
	}
	.content {
		margin-top: 20px;
		display: flex;
		flex-direction: column;
		align-items: center;
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
	}
	.form {
		width: 90%;
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
	.error-message {
        font: var(--primary-font-regular);
        font-size: 12px;
        color: var(--red);
        margin-bottom: 15px;
        margin-top: -10px;
    }
	@media only screen and (max-width: 966px) {
		.content {
			align-items: flex-start;
		}
		.form {
			margin-left: 10px;
		}
		.side-by-side {
            display: block
        }
	}
</style>
