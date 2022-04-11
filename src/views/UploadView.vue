<script>
import UploadForm from '@/components/UploadForm.vue'
export default {
  
    data() {
        return {
            description: "description",
            photo: undefined,
            message: "Lab 7 "
        };
    },
    components: { UploadForm }
}
</script>

<template>
    <div class="container">
      <div class="text-center">
        <h1>{{ message }}</h1>
        <UploadForm/>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
</style>