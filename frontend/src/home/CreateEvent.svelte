<script>
	import TextInput from "@/components/TextInput.svelte";
	import ActionButton from "@/components/ActionButton.svelte";
	import Button from "@/components/Button.svelte";
	import DatePicker from "@/components/DatePicker.svelte";
	import TimePicker from "@/components/TimePicker.svelte";
	import Header from "@/components/Header.svelte";
	import SpeakerField from "@/home/components/SpeakerField.svelte";

	import Event from "@/services/event.js";

	import { idIncrement, listTopics, storeEventTopics, alert } from "@/components/stores.js";

	import Speaker from "@/services/speaker.js";
	import { onMount, onDestroy } from "svelte";
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
		$storeEventTopics = [{ id: 1, title: "", hook: "", why: "", what: "", speakers, speaker: 0 }];
		$listTopics = [{ title: "", hook: "", why: "", what: "" }];
	});

	onDestroy(() => {
		$listTopics = [];
		$storeEventTopics = []
		$idIncrement = 0
	});

	$idIncrement = 2

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

	let loading = false;

	function addSpeaker() {
		if (!loading) {
			var l = $storeEventTopics.length; // get our current items list count
			$storeEventTopics[l] = { 
				id: $idIncrement, title: "", hook: "", why: "", what: "", speakers, speaker: 0 
			};
			$listTopics[l] = { 
				title: "", hook: "", why: "", what: ""
			};
			$idIncrement++; // increment our id to add additional items
		}
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

		for (let i = 0; i < $listTopics.length; i++) {
			
			if ($listTopics[i].selectedSpeaker == undefined || $listTopics[i].title == "" || $listTopics[i].hook == "" ||
				$listTopics[i].why == "" || $listTopics[i].what == "") {
					topicError.message = "Please fill in all the topic fields"
					return topicError.enabled = true
			} else {
				topicError.enabled = false
			}

			let topic = {
				speaker: $listTopics[i].selectedSpeaker,
				title: $listTopics[i].title,
				hook: $listTopics[i].hook,
				why: $listTopics[i].why,
				what: $listTopics[i].what,
			};
			topics.push(topic);
		}

		loading = true

		try {
			await Event.createEvent({
				episode: parseInt(episodeValue, 10),
				datetime,
				topic: topics,
			});

			pushState("/home")
		} catch {
			$alert.message = "Server error..."
			$alert.enabled = true
			loading = false;
		}
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
			<div class="form-wrapper">
				<div class="form">
					<div>
						<TextInput
							bind:instance={episode}
							label="Tech Night Episode"
							placeholder="Tech Night Episode"
							error={episodeError}
							type="number"
							disabled={loading ? true : false}
						/>
					</div>
					<div>
						{#each $storeEventTopics as item}
							<svelte:component this={SpeakerField} objAttributes={item} disabled={loading ? true : false}/>
						{/each}
						<div class="add-topic-div">
							<ActionButton on:click={addSpeaker} disabled={loading ? true : false}/>
						</div>
						{#if topicError.enabled}
							<p class="error-message">{topicError.message}</p>
						{/if}
					</div>
					<div class="side-by-side">
						<DatePicker bind:date error={dateError} disabled={loading ? true : false}/>
						<TimePicker bind:time error={timeError} disabled={loading ? true : false}/>
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
						<Button style="width: 50%" label="PUBLISH" on:click={publish} {loading}/>
					</div>
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
	.form-wrapper {
		display: flex;
		justify-content: center;
	}
	.form {
		width: 50vw;
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
		.form {
			width: 80vw;
			margin-left: -15px;
		}
		.side-by-side {
            display: block
        }
	}
</style>
