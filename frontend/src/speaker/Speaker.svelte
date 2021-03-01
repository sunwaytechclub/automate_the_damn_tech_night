<script>
    import SideNavbar from "@/components/SideNavbar.svelte"
    import Header from "@/components/Header.svelte"
    import ActionButton from "@/components/ActionButton.svelte"
    import Dragndrop from "@/components/Dragndrop.svelte"
    import AlertDialog from "@/components/AlertDialog.svelte"
    import TextInput from "@/components/TextInput.svelte"
    import Button from "@/components/Button.svelte"
    import pushState from "@/utils/pushState.js"

    import getLastSegUrl from "@/utils/getLastSegUrl.js"
    import { onMount } from "svelte";
    import Speaker from "@/services/speaker.js"

    let speakerId = getLastSegUrl()
    let speaker = {};

    onMount(async () => {
        let data = await Speaker.getSpeaker({
            id: speakerId
        })
        speaker = data
        // name = speaker.name
        // position = speaker.position
        // avatar = speaker.avatar
        })

    let name = "";
    let position = "";
    let avatar;

    let nameError = {};
    let positionError = {};
    let avatarError = {
        enabled: false,
        message: "Invalid"
    }
    let loading;

    let avatarElement

    let deleteDialog = false;

    async function editSpeaker() {

        let nameValue = name.value
        let positionValue = position.value

        if (nameValue == "") {
            nameError.enabled = true;
            nameError.message = "Please fill in speaker name"
            return
        } else {
            nameError.enabled = false;
        }

        if (positionValue == "") {
            positionError.enabled = true;
            positionError.message = "Please fill in speaker position"
            return
        } else {
            positionError.enabled = false;
        }

        loading = true;

        let response = await Speaker.updateSpeaker({
            id: speakerId,
            name: name.value,
            position: position.value,
            avatar: avatar || null
        })
        console.log(response)
        location.reload()
    }

    function showDeleteDialog() {
        deleteDialog = true
    }

    async function deleteSpeaker() {
        
        let response = await Speaker.deleteSpeaker({
            id: speakerId
        })
        console.log(response)
        pushState("/speakers")
    }
</script>

<div class="wrapper">
    <SideNavbar/>
    <div class="content">
        <Header title="Edit speaker" previousPath="/speakers"/>
        <div class="page-subheader">
			<p class="subheader-text">Create new speaker</p>
            <ActionButton label="Delete Speaker" 
                    iconPath="/assets/icons/user-x-red.svg" 
                    textColor="var(--red)" on:click={showDeleteDialog}/>
		</div>
        {#await speaker}
            <!-- TODO: loader -->
        {:then}
        
            <div class="form">
                <div>
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label>Avatar</label>
                    <div class="avatar-div">
                        <div class="dialog-div">
                            <p class="alert-dialog-title">Current avatar: </p>
                            <img src={speaker.avatar} alt="" class="avatar" bind:this={avatarElement}/>
                        </div>
                        <!-- <ActionButton label="Upload new avatar" iconPath="/assets/icons/upload-yellow.svg" on:click={showUploadDialog}/> -->
                        <div class="dialog-div">
                            <p class="alert-dialog-title">Upload new avatar: </p>
                            <div class="dragdrop-div">
                                <Dragndrop bind:file={avatar}/>
                                {#if avatarError.enabled}
                                    <p class="error-message">{avatarError.message}</p>
                                {:else}
                                    <div class="error-spacer"></div>
                                {/if}
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <TextInput value={speaker.name} label="Name" placeholder="Name" bind:instance={name} error={nameError} disabled={loading ? true : false}/>
                </div>
                <div>
                    <TextInput value={speaker.position} label="Position" placeholder="Position" bind:instance={position} error={positionError} disabled={loading ? true : false}/>
                    <!-- {#each $storeFE as item}
                    <svelte:component this={PositionField} objAttributes={item}/>
                    {/each}
                    <div class="add-topic-div">
                        <ActionButton label="Add Position"/>
                    </div> -->
                </div>
                <div class="confirm-button-div">
                    <Button style="width: 50%" label="CONFIRM" on:click={editSpeaker} {loading}/>
                </div>
            </div>

        {/await}
    </div>
</div>

{#if deleteDialog}
    <AlertDialog bind:visible={deleteDialog}>
        <p class="title">Are you sure?</p>
        <p class="message">Are you sure want to delete {speaker.name}?</p>
        <div class="button-div">
            <Button secondaryButton label="Cancel" on:click={() => deleteDialog=false}/>
            <Button on:click={deleteSpeaker} label="Yes"/>
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
        margin-top: 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    .form {
        width: 70%;
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
        height: 200px
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
</style>