<script>
	import Header from "@/components/Header.svelte";
	import ActionButton from "@/components/ActionButton.svelte";
	import Dragndrop from "@/components/Dragndrop.svelte";
	import AlertDialog from "@/components/AlertDialog.svelte";
	import TextInput from "@/components/TextInput.svelte";
	import Button from "@/components/Button.svelte";
	import pushState from "@/utils/pushState.js";
	import PositionField from "@/speaker/components/PositionField.svelte";

	import getLastSegUrl from "@/utils/getLastSegUrl.js";
	import SpeakerAPI from "@/services/speaker.js";

	import { storeSpeaker, idIncrement, storeSpeakerPositions, listPositions, alert} from "@/components/stores.js";
	import { onMount, onDestroy } from "svelte";

	let speakerId = getLastSegUrl();
	let speaker = {};
	let positions = []
	
	onMount(async () => {
		let data = await SpeakerAPI.getSpeaker({
			id: speakerId,
		});
		speaker = data;
		$storeSpeaker = speaker
		
		let tempPositions = speaker.position.split("\n")
		
		for (let i = 0; i < tempPositions.length; i++) {
			let positionObj = {
				id: i + 1,
				position: tempPositions[i],
				deleteButton: false
			}
			$listPositions.push(tempPositions[i])
			$storeSpeakerPositions.push(positionObj)
		}
		positions = $storeSpeakerPositions
		$idIncrement = $storeSpeakerPositions.length + 1
		if ($storeSpeakerPositions.length > 1) {
			$storeSpeakerPositions[$storeSpeakerPositions.length - 1].deleteButton = true
		}
	});

	onDestroy(() => {
		$listPositions = [];
		$storeSpeakerPositions = []
		$idIncrement = 0
	});
	
	let name = "";
	let avatar;
	let loading;
	let avatarElement;
	let deleteDialog = false;
	
	let nameError = {};
	let positionError = {};
	let avatarError = {
		enabled: false,
		message: "Invalid",
	};
	let maxPositionError = {
		enabled: false,
		message: "You can only add up to 4 positions"
	}

	function addPosition() {
		console.log($storeSpeakerPositions)
		var l = $storeSpeakerPositions.length; // get our current items list count
		if (l > 3) {
			return maxPositionError.enabled = true
		} 
		$storeSpeakerPositions[l] = {
			id: $idIncrement,
			position: "",
			deleteButton: true
		};
		$storeSpeakerPositions[l-1].deleteButton = false
		$idIncrement++; // increment our id to add additional items
	}

	async function editSpeaker() {
		let nameValue = name.value;
		let positionValue = ""

		if (nameValue == "") {
			nameError.enabled = true;
			nameError.message = "Please fill in speaker name";
			return;
		} else {
			nameError.enabled = false;
		}

		for (let i = 0; i < $storeSpeakerPositions.length; i++) {

		if ($storeSpeakerPositions[i].position.value == "") {
				positionError.message = "Please fill in position(s)"
				return positionError.enabled = true
			}

			let position = $storeSpeakerPositions[i].position.value

			positionValue += `${position}\n`;
		}

		loading = true;

		try {
			SpeakerAPI.updateSpeaker({
				id: speakerId,
				name: name.value,
				position: positionValue,
				avatar: avatar || null,
			});
			
			location.reload();
		} catch {
			$alert.message = "Server error..."
			$alert.enabled = true
			loading = false;
		}

	}

	
	async function deleteSpeaker() {
		try {
			await SpeakerAPI.deleteSpeaker({
				id: speakerId,
			});
			
			pushState("/speakers");
		} catch {
			$alert.message = "Server error..."
			$alert.enabled = true
			loading = false;
		}
	}

	function showDeleteDialog() {
		deleteDialog = true;
	}

	async function deletePosition() {
		let tempPositions = $storeSpeakerPositions
		tempPositions.pop()
		$listPositions.pop()
		$idIncrement--

		$storeSpeakerPositions = tempPositions

		if ($storeSpeakerPositions.length == 2) {
			$storeSpeakerPositions[1].deleteButton = true
		}
	}
</script>

<div class="wrapper">
	<div class="content">
		<Header title="Edit speaker" previousPath="/speakers" />
		<div class="page-subheader">
			<p class="subheader-text">Create new speaker</p>
			<ActionButton
				label="Delete Speaker"
				iconPath="/assets/icons/user-x-red.svg"
				textColor="var(--red)"
				on:click={showDeleteDialog}
			/>
		</div>
		{#if positions.length == 0}
			<!-- TODO: loader -->
		{:else}
			<div class="form">
				<div>
					<!-- svelte-ignore a11y-label-has-associated-control -->
					<label>Avatar</label>
					<div class="avatar-div">
						<div class="dialog-div">
							<p class="alert-dialog-title">Current avatar:</p>
							<img
								src={speaker.avatar}
								alt=""
								class="avatar"
								bind:this={avatarElement}
							/>
						</div>
						<!-- <ActionButton label="Upload new avatar" iconPath="/assets/icons/upload-yellow.svg" on:click={showUploadDialog}/> -->
						<div class="dialog-div">
							<p class="alert-dialog-title">Upload new avatar:</p>
							<div class="dragdrop-div">
								<Dragndrop bind:file={avatar} />
								{#if avatarError.enabled}
									<p class="error-message">{avatarError.message}</p>
								{:else}
									<div class="error-spacer" />
								{/if}
							</div>
						</div>
					</div>
				</div>
				<div>
					<TextInput
						value={speaker.name}
						label="Name"
						placeholder="Name"
						bind:instance={name}
						error={nameError}
						disabled={loading ? true : false}
					/>
				</div>
				<div>
					{#each $storeSpeakerPositions as item, i}
                		<svelte:component this={PositionField} objAttributes={item} disabled={loading ? true : false} on:delete={deletePosition}/>
					{/each}
					<div class="add-topic-div">
						<ActionButton label="Add Position" on:click={addPosition}/>
					</div>
					{#if maxPositionError.enabled}
						<p class="error-message">{maxPositionError.message}</p>
					{/if}
					{#if positionError.enabled}
						<p class="error-message">{positionError.message}</p>
					{/if}
				</div>
				<div class="confirm-button-div">
					<Button
						style="width: 50%"
						label="CONFIRM"
						on:click={editSpeaker}
						{loading}
					/>
				</div>
			</div>
		{/if}
	</div>
</div>

{#if deleteDialog}
	<AlertDialog bind:visible={deleteDialog}>
		<p class="title">Are you sure?</p>
		<p class="message">Are you sure want to delete {speaker.name}?</p>
		<div class="button-div">
			<Button
				secondaryButton
				label="Cancel"
				on:click={() => (deleteDialog = false)}
			/>
			<Button on:click={deleteSpeaker} label="Yes" />
		</div>
	</AlertDialog>
{/if}

<style>
	label {
		font-weight: 600;
		margin-bottom: 10px;
		display: block;
		color: var(--dark-blue);
	}
	.wrapper {
		width: 100%;
		display: flex;
	}
	.content {
		margin-top: 20px;
		display: flex;
		flex-direction: column;
		width: 95%;
	}
	.form {
		width: 100%;
	}
	.page-subheader {
		display: flex;
		align-items: center;
		justify-content: space-between;
		border-bottom: 2px var(--light-grey) solid;
		padding-bottom: 10px;
		margin-bottom: 20px;
		width: 95%;
	}
	.subheader-text {
		font: var(--primary-font-regular);
		font-size: 10px;
		color: var(--dark-blue);
	}
	.avatar-div {
		display: flex;
		align-items: flex-end;
		margin-bottom: 30px;
	}
	.avatar {
		margin-right: 30px;
		width: 200px;
		height: 200px;
	}
	.confirm-button-div {
		width: 100%;
		display: flex;
		justify-content: center;
		margin: 40px 0;
	}
	.dialog-div {
		display: flex;
		justify-content: center;
		flex-direction: column;
	}
	.alert-dialog-title {
		font: var(--primary-font-medium);
		margin-bottom: 10px;
		font-size: 12px;
	}
	.title {
		font: var(--primary-font-bold);
		font-size: 24px;
		margin-bottom: 20px;
	}
	.message {
		margin-bottom: 40px;
	}
	.button-div {
		display: grid;
		grid-template-columns: auto auto;
		column-gap: 30px;
	}
	.error-message {
		font: var(--primary-font-regular);
		font-size: 12px;
		color: var(--red);
		margin-bottom: 15px;
		margin-top: 5px;
		position: absolute;
	}
	@media only screen and (max-width: 966px) {
		.content {
			align-items: center;
		}
		.avatar-div {
			flex-direction: column;
			align-items: center;
		}
		.avatar {
			margin-right: 0;
			margin-bottom: 10px;
		}
		.button-div {
			display: block;
		}
		.form {
			width: 80%;
		}
	}
</style>
