<script>
    export let visible = false;
</script>

{#if visible}
        <div class="blur-background">
            <div class="alert-div">
                <img src="/assets/icons/close-big.svg" alt="" class="close" on:click={()=>{visible = false}}/>
                <slot></slot>
            </div>
        </div>
{/if}

<style>
    .blur-background {
        position: fixed;
        top: 0;
        left: 0;
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
        position: relative;
    }
    .close {
        position: absolute;
        right: 20px;
        top: 20px;
        cursor: pointer;
    }
    @media only screen and (max-width: 600px) {
		.alert-div {
            min-width: 0;
            width: 350px;
        }
	}
</style>