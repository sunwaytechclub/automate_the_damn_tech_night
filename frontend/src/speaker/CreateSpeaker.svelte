<script>
	import Header from "@/components/Header.svelte";
	import ActionButton from "@/components/ActionButton.svelte";
	import Dragndrop from "@/components/Dragndrop.svelte";
	import PositionField from "@/speaker/components/PositionField.svelte";
	import TextInput from "@/components/TextInput.svelte";
	import Button from "@/components/Button.svelte";

	import Speaker from "@/services/speaker.js";
	import pushState from "@/utils/pushState";

	import { idIncrement, storeSpeakerPositions, listPositions, alert } from "@/components/stores.js";
	import { onDestroy } from 'svelte'

	onDestroy(() => {
		$listPositions = [];
		$storeSpeakerPositions = []
		$idIncrement = 0
	});

	let name;
	let avatar;
	let positions = ""
	let maxPositionError = {
		enabled: false,
		message: "You can only add up to 3 positions"
	}
	
	let loading;
	let nameError = {};
	let positionError = {};
	let avatarError = {
		enabled: false,
		message: "Invalid",
	};

	$storeSpeakerPositions = [
		{ id: 1, position: ""},
	];

	$idIncrement = 2

	function addPosition() {
		var l = $storeSpeakerPositions.length; 
		if (l >= 3) {
			return maxPositionError.enabled = true
		} 
		$storeSpeakerPositions[l] = {
			id: $idIncrement,
			position: "",
			deleteButton: true
		};
		$storeSpeakerPositions[l-1].deleteButton = false
		$idIncrement++;
	}

	async function createSpeaker() {
		let nameValue = name.value;

		if (nameValue == "") {
			nameError.enabled = true;
			nameError.message = "Please fill in speaker name";
			return;
		} else {
			nameError.enabled = false;
		}

		if (avatar == null) {
			avatarError.enabled = true;
			avatarError.message = "Please upload an avatar";
			return;
		} else {
			avatarError.enabled = false;
		}

		for (let i = 0; i < $storeSpeakerPositions.length; i++) {

			if ($storeSpeakerPositions[i].position.value == "") {
					positionError.message = "Please fill in position(s)"
					return positionError.enabled = true
			}

			let position = $storeSpeakerPositions[i].position.value
			
			positions += `${position}\n`;
		}

		loading = true;

		try {
			await Speaker.createSpeaker({
				name: nameValue,
				position: positions,
				avatar,
			});

			pushState("/speakers");
		} catch {
			$alert.message = "Server error..."
			$alert.enabled = true
			loading = false;
		}
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
		<Header title="New speaker" previousPath="/speakers" />
		<div class="page-subheader">
			<p class="subheader-text">Create new speaker</p>
		</div>
		<div class="form-wrapper">
			<div class="form">
				<div>
					<!-- svelte-ignore a11y-label-has-associated-control -->
					<label>Avatar</label>
					<div class="upload-div-wrapper">
						<div class="upload-div">
							<Dragndrop bind:file={avatar} />

							{#if avatarError.enabled}
								<p class="error-message">{avatarError.message}</p>
							{:else}
								<div class="error-spacer" />
							{/if}
						</div>
					</div>
				</div>
				<div>
					<TextInput
						bind:instance={name}
						label="Name"
						placeholder="Name"
						error={nameError}
						disabled={loading ? true : false}
					/>
				</div>
				<div>
					<!-- <TextInput
						bind:instance={position}
						label="Position"
						placeholder="Position"
						error={positionError}
						disabled={loading ? true : false}
					/> -->
					{#each $storeSpeakerPositions as item}
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
						on:click={createSpeaker}
						{loading}
					/>
				</div>
			</div>
		</div>
	</div>
</div>

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
		width: 100%;
	}
	.form-wrapper {
		display: flex;
		justify-content: center;
	}
	.form {
		width: 50vw;
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
	.upload-div {
		height: 200px;
		width: 200px;
		margin-bottom: 30px;
	}
	.confirm-button-div {
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
		margin-top: 5px;
	}
	.error-spacer {
		height: 20px;
	}
	@media only screen and (max-width: 966px) {
		.content {
			align-items: center;
		}
		.form {
			width: 80vw;
			margin-left: -15px;
		}
		.upload-div-wrapper {
			display: flex;
			justify-content: center;
		}
	}
</style>
