<script setup lang="ts">
withDefaults(defineProps<{ title?: string; note?: string }>(), {})
</script>

<template>
  <section class="equation-block">
    <div v-if="title" class="equation-title">{{ title }}</div>
    <div class="equation-content"><slot /></div>
    <div v-if="note" class="equation-note">{{ note }}</div>
  </section>
</template>

<style scoped>
.equation-block { border-left: 3px solid var(--slidev-theme-primary, currentColor); padding: .65rem 1rem; margin: .8rem 0; background: color-mix(in srgb, var(--slidev-theme-primary, currentColor) 5%, transparent); }
.equation-title { font-weight: 650; margin-bottom: .35rem; }
.equation-content { text-align: center; font-size: 1.08em; }
.equation-note { margin-top: .35rem; font-size: .72em; opacity: .7; }
</style>
