<template>
    <v-list
        :items="items"
        item-props
        lines="three"
    >
        <template v-slot:subtitle="{ subtitle }">
        <div v-html="subtitle"></div>
        </template>
    </v-list>
</template>

<script setup lang="ts">
  import { ref, defineProps, defineEmits } from 'vue'
  import * as fetchAPI from '@/assets/ts/fetch.ts'

  const props = defineProps({ newsId: Number })

  const commentList = ref([])
  const items = ref([])
  let call_func = true

  function commentProcess(){
    if(commentList.value.length >= 1){
      for (var i = 0; i < commentList.value.length; i++) {
        const value = commentList.value[i]
        const tempo = {
          id: value.id,
          prependAvatar: value.avatar,
          title: value.username,
          subtitle: value.content,
        }
        items.value.push({ type: 'divider', inset: true }, tempo)
      }
      items.value.splice(0,1,{ type: 'subheader', title: 'Top comment' })
    }
  }

  window.onscroll = () => {
    if(call_func){
      let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight >= document.documentElement.offsetHeight - 500;
      if (bottomOfWindow) {
        call_func = false
        Promise.all([
          fetchAPI.fetchGetNewsComments(props.newsId),
        ]).then((values) => {
          commentList.value = values[0]
          commentProcess()
        });    
      }
    }
  }


</script>

<style>
</style>