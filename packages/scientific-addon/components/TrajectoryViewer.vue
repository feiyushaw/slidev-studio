<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

type Point = { x: number; y: number }
type Trajectory = { name?: string; points: Point[]; best?: boolean }
const props = withDefaults(defineProps<{ src?: string; trajectories?: Trajectory[]; width?: number; height?: number }>(), { width: 760, height: 380 })
const data = ref<Trajectory[]>(props.trajectories ?? [])
const step = ref(100)

onMounted(async () => {
  if (!data.value.length && props.src) data.value = await fetch(props.src).then(r => r.json())
})

const all = computed(() => data.value.flatMap(t => t.points))
const bounds = computed(() => {
  const xs = all.value.map(p => p.x), ys = all.value.map(p => p.y)
  return { minX: Math.min(...xs, 0), maxX: Math.max(...xs, 1), minY: Math.min(...ys, 0), maxY: Math.max(...ys, 1) }
})
function sx(x:number) { const b=bounds.value; return 24 + (x-b.minX)/(b.maxX-b.minX || 1)*(props.width-48) }
function sy(y:number) { const b=bounds.value; return props.height-24 - (y-b.minY)/(b.maxY-b.minY || 1)*(props.height-48) }
function path(t:Trajectory) {
  const n = Math.max(2, Math.ceil(t.points.length * step.value / 100))
  return t.points.slice(0,n).map((p,i)=>`${i?'L':'M'} ${sx(p.x)} ${sy(p.y)}`).join(' ')
}
</script>

<template>
  <div class="trajectory-viewer">
    <svg :viewBox="`0 0 ${width} ${height}`" role="img" aria-label="Trajectory visualization">
      <line v-for="i in 7" :key="`h${i}`" x1="0" :x2="width" :y1="i*height/8" :y2="i*height/8" class="grid" />
      <path v-for="(t,i) in data" :key="i" :d="path(t)" fill="none" :class="['traj', { best: t.best }]" />
    </svg>
    <label class="control">Progress <input v-model="step" type="range" min="5" max="100" step="5"> {{ step }}%</label>
  </div>
</template>

<style scoped>
.trajectory-viewer svg { width: 100%; max-height: 62vh; border: 1px solid color-mix(in srgb, currentColor 18%, transparent); border-radius: 8px; }
.grid { stroke: currentColor; opacity: .08; }
.traj { stroke: currentColor; opacity: .32; stroke-width: 2; vector-effect: non-scaling-stroke; }
.traj.best { stroke: var(--slidev-theme-primary, currentColor); opacity: 1; stroke-width: 4; }
.control { display:flex; align-items:center; gap:.55rem; margin-top:.45rem; font-size:.72em; opacity:.8; }
.control input { flex:1; }
</style>
