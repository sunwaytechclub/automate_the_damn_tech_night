<script>
	import { fade } from "svelte/transition";
</script>

<div class="wrapper" transition:fade={{ duration: 100 }}>
	<slot />
</div>

<style>
	.wrapper {
		background: #ffffff;
		box-shadow: 2px 7px 24px rgba(0, 0, 0, 0.09);
		border-radius: 5px;
		width: 100%;
	}
</style>
