<script>
    import { onDestroy } from "svelte";
	import { disableNavbar } from "@/utils/store";

	$disableNavbar = true;

	onDestroy(() => ($disableNavbar = false));
</script>

<h1>404 not found</h1>
