<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

const open = ref(false)
const pathname = ref('')

onMounted(() => {
  pathname.value = window.location.pathname
})

const base = computed(() => {
  const viteBase = import.meta.env.BASE_URL || '/'
  const trimmed = viteBase.replace(/\/(scholarly|hep|business)\/?$/, '')
  return trimmed === '/' ? '' : trimmed.replace(/\/$/, '')
})

const current = computed(() => {
  const path = `${pathname.value} ${import.meta.env.BASE_URL}`
  if (path.includes('/scholarly')) return 'scholarly'
  if (path.includes('/hep')) return 'hep'
  if (path.includes('/business')) return 'business'
  return ''
})

const items = [
  { id: 'scholarly', label: 'Scholarly', meta: 'Academic' },
  { id: 'hep', label: 'HEP', meta: 'Technical' },
  { id: 'business', label: 'Tahta', meta: 'Business' },
]

function href(id: string) {
  return `${base.value}/${id}/`.replace(/\/\//g, '/')
}

function homeHref() {
  return `${base.value}/`.replace(/\/\//g, '/')
}
</script>

<template>
  <div class="studio-theme-switcher">
    <button
      class="studio-theme-button"
      type="button"
      aria-label="Switch presentation theme"
      :aria-expanded="open"
      @click="open = !open"
    >
      ◈
    </button>

    <div v-if="open" class="studio-theme-menu">
      <a class="studio-home" :href="homeHref()">Slidev Studio</a>
      <a
        v-for="item in items"
        :key="item.id"
        :href="href(item.id)"
        :class="['studio-theme-item', { active: current === item.id }]"
      >
        <span>{{ item.label }}</span>
        <small>{{ item.meta }}</small>
      </a>
    </div>
  </div>
</template>

<style scoped>
.studio-theme-switcher {
  position: fixed;
  top: 14px;
  right: 16px;
  z-index: 10000;
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.studio-theme-button {
  width: 34px;
  height: 34px;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  background: color-mix(in srgb, var(--slidev-slide-container-background, white) 88%, transparent);
  color: inherit;
  backdrop-filter: blur(10px);
  cursor: pointer;
  box-shadow: 0 8px 24px rgba(0,0,0,.12);
}
.studio-theme-menu {
  margin-top: 8px;
  width: 176px;
  padding: 8px;
  border-radius: 12px;
  border: 1px solid color-mix(in srgb, currentColor 14%, transparent);
  background: color-mix(in srgb, var(--slidev-slide-container-background, white) 94%, transparent);
  backdrop-filter: blur(14px);
  box-shadow: 0 16px 42px rgba(0,0,0,.16);
}
.studio-home,
.studio-theme-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 8px 10px;
  border-radius: 8px;
  color: inherit;
  text-decoration: none;
}
.studio-home { font-weight: 650; margin-bottom: 4px; }
.studio-theme-item:hover,
.studio-theme-item.active { background: color-mix(in srgb, currentColor 8%, transparent); }
.studio-theme-item small { opacity: .55; font-size: 10px; }
.studio-theme-item.active::before { content: "•"; margin-right: 2px; }
</style>
