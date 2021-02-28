<script>
    import SideNavbar from "@/components/SideNavbar.svelte"
    import Header from "@/components/Header.svelte"
    import ActionButton from "@/components/ActionButton.svelte"
    import Dragndrop from "@/components/Dragndrop.svelte"
    import AlertDialog from "@/components/AlertDialog.svelte"
    import PositionField from "@/speaker/components/PositionField.svelte"
    import TextInput from "@/components/TextInput.svelte"
    import Button from "@/components/Button.svelte"

    import { storeFE, idIncrement } from '@/components/stores.js';

    let date = " 26 Feb 2021"
    let speakers = [
        {value: 'rain', label: 'Rain Chai'},
        {value: 'nick', label: 'Nick'},
        {value: 'yong', label: 'Yong'},
        {value: 'lynus', label: 'Lynus'},
        {value: 'eason', label: 'Eason'},
    ];

    $storeFE = [
		{ id:1, topic: 'First option', caption: "additional note", speakers }
            // other items can go here
    ];

    idIncrement.set(2); // this is a crude way to increment the id for new items

    function addPosition() {
        var l = $storeFE.length;	// get our current items list count
		$storeFE[l] = { id:$idIncrement, topic: 'Another option', caption: "additional note", speakers };
		console.log($storeFE);
		$idIncrement++;	// increment our id to add additional items
    }
</script>

<div class="wrapper">
    <SideNavbar/>
    <div class="content">
        <Header title="New speaker" previousPath="/speakers"/>
        <div class="page-subheader">
			<p class="subheader-text">Create new speaker</p>
		</div>
        <div class="form">
            <div>
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label>Avatar</label>
                <div class="upload-div">
                    <Dragndrop/>
                </div>
            </div>
            <div>
                <TextInput label="Name" placeholder="Name"/>
            </div>
            <div>
                {#each $storeFE as item}
                <svelte:component this={PositionField} objAttributes={item}/>
                {/each}
                <div class="add-topic-div">
                    <ActionButton label="Add Position" on:click={addPosition}/>
                </div>
            </div>
            <div class="confirm-button-div">
                <Button style="width: 50%" label="CONFIRM"/>
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
        margin-top: 50px;
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
    .avatar {
        margin-right: 30px;
    }
    .add-topic-div {
        border-bottom: 2px var(--light-grey) solid;
        padding-bottom: 15px;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .confirm-button-div {
        width: 100%;
        display: flex;
        justify-content: center;
        margin: 40px 0;
    }
    .alert-dialog {
        display: flex;
        justify-content: center;
    }
    .dialog-div {
        display: flex;
        justify-content: center;
        flex-direction: column;
    }
    .alert-dialog-title {
        font: var(--primary-font-bold);
        margin-bottom: 20px;
        font-size: 18px;
    }
    .alert-dialog-text {
        font: var(--primary-font-regular);
        font-size: 12px;
    }
</style>