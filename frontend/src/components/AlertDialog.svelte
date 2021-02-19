<script>
    import Button from "@/components/Button.svelte";
    export let visible = false;
</script>

{#if visible}
    <div class="blur-background">
        <div class="alert-div">
            <p class="title">Are you sure?</p>
            <p class="message">Are you sure want to delete Speaker #2?</p>
            <div class="button-div">
                <Button secondaryButton on:click={() => visible=false}/>
                <Button on:click/>
            </div>
        </div>
    </div>
{/if}

<style>
    .blur-background {
        position: fixed;
        top: 0;
        height: 100vh;
        width: 100vw;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 1;
        display: grid;
        place-items: center;
    }
    .alert-div {
        z-index: 2;
        background-color: var(--white);
        padding: 40px;
        border-radius: 5px;
        max-width: 700px;
        min-width: 600px;
    }
    .title {
        font: var(--primary-font-bold);
        font-size: 24px;
        margin-bottom: 20px;
    }
    .message {
        font: var(--primary-font-semibold);
        margin-bottom: 40px;
    }
    .button-div {
        display: grid;
        grid-template-columns: auto auto;
        column-gap: 30px;
    }
</style>