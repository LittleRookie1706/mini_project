import { createApp } from 'vue'
import App from './App.vue'
import { loadFonts } from './plugins/webfontloader'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
// import colors from 'vuetify/lib/util/colors'

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
  },

  // theme: {
  //   themes: {
  //     light: {
  //       dark: false,
  //       colors: {
  //         primary: colors.red.darken1, // #E53935
  //         secondary: colors.red.lighten4, // #FFCDD2
  //         ...
  //       }
  //     },
  //   },
  // },

})

loadFonts()

createApp(App)
  .use(vuetify)
  .mount('#app')
