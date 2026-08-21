<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

type Iteration = { iteration: number; objective: number; candidates?: number[] }
const props = defineProps<{ src?: string; iterations?: Iteration[] }>()
const data = ref<Iteration[]>(props.iterations ?? [])
const index = ref(0)

onMounted(async () => {
  if (!data.value.length && props.src) data.value = await fetch(props.src).then(r => r.json())
})
const current = computed(() => data.value[Math.min(index.value, Math.max(data.value.length - 1, 0))])
const maxObj = computed(() => Math.max(...data.value.map(d => d.objective), 1))
</script>

<template>
  <div class="opt-viewer" v-if="data.length">
    <div class="summary">
      <div><b>Iteration</b><span>{{ current.iteration }}</span></div>
      <div><b>Objective</b><span>{{ current.objective.toPrecision(4) }}</span></div>
      <div><b>Candidates</b><span>{{ current.candidates?.length ?? 0 }}</span></div>
    </div>
    <div class="spark" aria-label="Objective history">
      <div v-for="(d,i) in data" :key="i" class="bar" :class="{ active: i <= index }" :style="{ height: `${Math.max(4, d.objective / maxObj * 100)}%` }" />
    </div>
    <label>Iteration
      <input v-model.number="index" type="range" min="0" :max="data.length - 1" step="1">
    </label>
  </div>
</template>

<style scoped>
.opt-viewer { width:100%; }
.summary { display:grid; grid-template-columns:repeat(3,1fr); gap:.7rem; margin-bottom:.7rem; }
.summary > div { border:1px solid color-mix(in srgb,currentColor 16%,transparent); border-radius:8px; padding:.55rem .7rem; }
.summary b { display:block; font-size:.62em; opacity:.6; }
.summary span { font-size:1.15em; }
.spark { height:210px; display:flex; gap:3px; align-items:flex-end; border-bottom:1px solid color-mix(in srgb,currentColor 20%,transparent); }
.bar { flex:1; background:currentColor; opacity:.12; min-width:2px; }
.bar.active { background:var(--slidev-theme-primary,currentColor); opacity:.8; }
label { display:flex; gap:.6rem; align-items:center; margin-top:.55rem; font-size:.72em; }
input { flex:1; }
</style>
