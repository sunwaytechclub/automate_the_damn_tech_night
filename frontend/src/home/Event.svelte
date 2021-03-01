<script>
    import SideNavbar from "@/components/SideNavbar.svelte"
    import Header from "@/components/Header.svelte"
    import ActionButton from "@/components/ActionButton.svelte"
    import getLastSegUrl from "@/utils/getLastSegUrl.js"
    import { onMount } from "svelte";
    import marked from "marked"

    import EventAPI from "@/services/event.js"

    let eventId = getLastSegUrl()

    let event = {};
    let writeupContainer
    let content;

    onMount(async () => {
        let data  = await EventAPI.getEvent({
            id: eventId
        })
        event = data;
        content = event.writeup
        event.writeup = event.writeup.replace(/\n/g,"<br />");
        writeupContainer.innerHTML = event.writeup
    })

    let date = " 26 Feb 2021"

    function downloadWriteup() {
        console.log(content.text())
        document.execCommand("copy")
    }

    async function downloadPoster() {
        const response = await fetch(event.poster)
        const object = await response.blob()
        const objectURL = URL.createObjectURL(object)
        const link = document.createElement('a'); 
        link.href = objectURL; 
        link.setAttribute('download', `tech-night-poster-#${event.episode}.jpg`); 
        link.setAttribute('style', 'display: none');
        document.body.appendChild(link); 
        link.click();
    }
</script>

<div class="wrapper">
    <SideNavbar/>
    <div class="content">
        {#await event}
            <!-- TODO: loader -->
        {:then}
        <Header title="Tech Night #{event.episode}" previousPath="/home"/>
        <div class="page-subheader">
			<p class="subheader-text">{date}</p>
		</div>
        <div class="generated-content line">
            <div class="field-title">
                <p class="field-title-text">Generated Content</p>
                <ActionButton label="Copy" 
                    iconPath="/assets/icons/copy.svg" 
                    textColor="var(--dark-blue)" on:click={downloadWriteup}/>
            </div>
            <div class="content-writeup" bind:this={writeupContainer}>
            </div>
        </div>
        <div class="generated-poster line">
            <div class="field-title">
                <p class="field-title-text">Generated Poster</p>
                <ActionButton label="Download" 
                    iconPath="/assets/icons/download.svg" 
                    textColor="var(--dark-blue)" on:click={downloadPoster}/>
            </div>
            <img src={event.poster} alt="" class="poster"/>
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
        margin-top: 40px;
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
        color: var(--dark-blue);
	}
    .field-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    .field-title-text {
        font: var(--primary-font-semibold)
    }
    .content-writeup {
        background-color: var(--light-grey);
        padding: 30px;
        width: 750px;
    }
    .poster {
        width: 750px;
    }
    .line {
        padding-bottom: 20px;
        border-bottom: 2px var(--light-grey) solid;
        margin-bottom: 30px;
    }
</style>