import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { loadFonts } from './plugins/webfontloader'

// vuetify and fa icon
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@fortawesome/fontawesome-free/css/all.css' // Ensure your project is capable of handling css files
import { aliases, fa } from 'vuetify/iconsets/fa'

const vuetify = createVuetify({
  components,
  directives,

  icons: {
    defaultSet: 'fa',
    aliases,
    sets: {
      fa,
    },
  }
})

loadFonts()

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app')
  