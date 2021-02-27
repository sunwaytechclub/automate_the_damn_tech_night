<script>
	import Dropzone from "svelte-file-dropzone";

	export let file = null;
	let base64;
	async function handleFileSelect(e) {
		const { acceptedFiles } = e.detail;
		file = acceptedFiles[0];
		base64 = await toBase64(acceptedFiles[0]);
	}

	function toBase64(file) {
		return new Promise((resolve, reject) => {
			const reader = new FileReader();
			reader.readAsDataURL(file);
			reader.onload = () => resolve(reader.result);
			reader.onerror = (error) => reject(error);
		});
	}
</script>

{#if base64}
	<div class="dropzone_area">
		<img src={base64} alt="uploaded" class="dropzone_area__image" />
		<div class="dropzone_area__edit" on:click={() => (base64 = null)}>
			<img src="/assets/icons/edit.svg" alt="edit" />
		</div>
	</div>
{:else}
	<Dropzone
		on:drop={handleFileSelect}
		multiple={false}
		containerStyles={`
        width:200px;
        height:200px;
        diplay:flex;
        justify-content:center;
        align-items:center;

        background:white;

        border: 1px dashed #000000;
        cursor: pointer;
    `}
	>
		<div class="inner">
			<img src="/assets/icons/upload.svg" alt="upload" />
			<p>Drop an image here or click to upload</p>
		</div>
	</Dropzone>
{/if}

<style>
	.dropzone_area {
		/* Layout */
		display: flex;
		justify-content: center;
		align-items: center;
		position: relative;

		width: 200px;
		height: 200px;
	}
	.dropzone_area__image {
		/* Layout */
		width: 100%;
	}
	.dropzone_area__edit {
		/* Layout */
		position: absolute;
		right: 5%;
		bottom: 5%;
		z-index: 2;

		display: flex;
		justify-content: center;
		align-items: center;

		width: 40px;
		height: 40px;

		/* Color */
		background-color: #fff;

		/* Effect */
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		cursor: pointer;
		border-radius: 50%;
	}
	.inner {
		/* Layout */
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}
	.inner p {
		/* Typography */
		font-size: 11px;
		text-align: center;

		/* Layout */
		margin-top: 10px;
	}
</style>
