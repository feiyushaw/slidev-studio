<script setup lang="ts">
withDefaults(defineProps<{ src: string; alt?: string; caption?: string; width?: string; objectFit?: 'contain' | 'cover' }>(), {
  alt: 'Scientific figure', width: '100%', objectFit: 'contain'
})
</script>

<template>
  <figure class="scientific-figure">
    <img :src="src" :alt="alt" :style="{ width, objectFit }" />
    <figcaption v-if="caption">{{ caption }}</figcaption>
  </figure>
</template>

<style scoped>
.scientific-figure { margin: 0; width: 100%; text-align: center; }
.scientific-figure img { display: block; max-height: 68vh; margin: 0 auto; }
.scientific-figure figcaption { margin-top: .55rem; font-size: .72em; opacity: .72; line-height: 1.35; }
</style>
