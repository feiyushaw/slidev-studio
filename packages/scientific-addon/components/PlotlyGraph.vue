<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref, watch } from 'vue'

const props = withDefaults(defineProps<{
  src?: string
  figure?: Record<string, any>
  height?: number
  config?: Record<string, any>
}>(), { height: 430 })

const el = ref<HTMLDivElement | null>(null)
let Plotly: any

async function loadFigure() {
  if (!el.value) return
  if (!Plotly) Plotly = (await import('plotly.js-dist-min')).default
  const spec = props.figure ?? (props.src ? await fetch(props.src).then(r => {
    if (!r.ok) throw new Error(`Failed to load ${props.src}: ${r.status}`)
    return r.json()
  }) : null)
  if (!spec) return
  await Plotly.react(el.value, spec.data ?? [], spec.layout ?? {}, {
    responsive: true,
    displaylogo: false,
    ...props.config,
  })
}

onMounted(loadFigure)
watch(() => [props.src, props.figure], loadFigure, { deep: true })
onBeforeUnmount(() => { if (Plotly && el.value) Plotly.purge(el.value) })
</script>

<template>
  <div ref="el" class="scientific-plotly" :style="{ height: `${height}px` }" />
</template>

<style scoped>
.scientific-plotly { width: 100%; min-height: 220px; }
</style>
