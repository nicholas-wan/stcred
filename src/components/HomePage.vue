<template>
  <div class="home_page">
    <div v-html="carouselHTML"></div>
    <!-- Use this whole chunk for the cards and module input field -->
    <br/><br/>
    <b-container fluid class="content">
      <b-row align-h="center">

        <b-col cols="4">
          <b-card no-body>
            <b-row no-gutters>
              <b-col md="4">
                <b-card-img src="https://www.nicholaswan.me/images/cheetah/computing.png" max-width="100%" height="100%" class="rounded-0" />
              </b-col>
              <b-col md="8">
                <b-card-body>
                  <router-link :to="{ name: 'course'}">
                    <div class="cardTitle1">Course</div>
                  </router-link>
                  <b-card-text>
                    <p class="text-left coursetext">
                      Find out when seniors are taking their Modules, and if you are taking it at a different time.
                    </p>
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
        </b-col>

        <b-col cols="4">
          <b-card no-body>
            <b-row no-gutters>
              <b-col md="4">
                <b-card-img src="https://www.nicholaswan.me/images/cheetah/arts.png" max-width="100%" height="100%" class="rounded-0" />
              </b-col>
              <b-col md="8">
                <b-card-body>
                  <router-link :to="{ name: 'modtype'}">
                    <div class="cardTitle2">Module Type</div>
                  </router-link>
                  <b-card-text>
                    <p class="text-left moduletext">
                        Search Modules based on Module Type, such as Language, General or Unrestricted Elective Modules.                    </p>
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
        </b-col>

        <b-col cols="4">
          <b-card no-body>
            <b-row no-gutters>
              <b-col md="4">
                <b-card-img src="https://www.nicholaswan.me/images/cheetah/industry.png" max-width="100%" height="100%" auto class="rounded-0" />
              </b-col>
              <b-col md="8">
                <b-card-body>
                  <router-link :to="{ name: 'industry'}">
                    <div class="cardTitle3">Industry</div>
                  </router-link>
                  <b-card-text>
                    <p class="text-left industrytext">
                      Discover Modules your alumni have taken based on their jobs and industries.
                    </p>
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
        </b-col>

      </b-row>

      <b-row align-h="center" height="300px">

        <b-col cols="12" class="categoryHeader">Search Individual Modules:</b-col>
        <b-col cols="4">
          <b-input-group>

            <b-form-input
              id="inputModuleCode"
              v-model="code"
              trim
              type="text"
              :state="checkModuleCode"
              aria-describedby="inputLiveHelp inputLiveFeedback"
              placeholder="Enter Module Code (e.g. ACC1002)"
            />
            <b-input-group-append>
              <router-link :to="{ name: 'module' }" :event="isInvalidInputR">
                <!-- <b-button :disabled="isInvalidInput" variant="dark" @click="updateCode">Search</b-button> -->
                <button :disabled="isInvalidInput" @click="updateCode"><div class="buttontext">Search</div></button>
              </router-link>
            </b-input-group-append>
            <!-- This will only be shown if the preceeding input has an invalid state -->
            <b-form-invalid-feedback id="inputLiveFeedback">
              Invalid Module Code
            </b-form-invalid-feedback>

          </b-input-group>

          <!-- Can be removed if unnecessary -->
          <b-form-text id="inputLiveHelp">
              Please do not enter the module name together with the module code
          </b-form-text>
        </b-col>
      </b-row>

      <br/><br/>
    </b-container>
    <br/><br/><br/>
    <Footer/>

    <v-tour name="myTour" :steps="steps" class="tourbox"></v-tour>

  </div>
</template>

<script>
  import Footer from "@/components/Footer.vue";
  import jsondata from '@/data/module_data.json';
  import { mapMutations } from 'vuex'  // Add mapMutations

  export default {

    data() {
      return {
        modulelist: jsondata['modulelist'],
        isInvalidInput: true,
        code: '',

        // For tour
        steps: [
          {
            target: '.banner',
            content: `Welcome to Modules+. Would you like a Tour?`
          },
          {
            target: '#inputModuleCode',
            content: `Search for a Module code here`
          },
          {
            target: '.coursetext',
            content: 'Click to find out more about people in your course',
          },
          {
            target: '.moduletext',
            content: 'Click to discover modules by their types',
          },
          {
            target: '.industrytext',
            content: 'Click to find out which modules are relevant for an industry',
          },
        ],
        carouselHTML: `
          <section class="banner full">
          <article class="slide">
            <img src="https://www.nicholaswan.me/images/cheetah/computing.png" alt="" />
            <div class="inner">
              <header>
                <p><a href="#">View modules done by seniors in your course</a></p>
                <h2>Course</h2>

              </header>
              <button class="button"> <a href="#/course">Explore More</a> </button>
            </div>
          </article>
          <article class="slide2 slide" >
            <img src="https://www.nicholaswan.me/images/cheetah/arts.png" alt="" />
            <div class="inner">
              <header>
                <p>View modules by type (e.g language, GE modules)</p>
                <h2>Module Type</h2>
              </header>
              <button class="button"> <a href="#/modtype">Explore More</a> </button>

            </div>
          </article>
          <article class="slide">
            <img src="https://www.nicholaswan.me/images/cheetah/industry.png"  alt="" />
            <div class="inner">
              <header>
                <p>View modules taken by graduates in an industry</p>
                <h2>Industry</h2>
              </header>
              <button class="button"> <a href="#/industry">Explore More</a> </button>

            </div>
          </article>
        </section>
      `
      }
    },
    mounted: function () {
      this.$tours['myTour'].start()
    },
    methods: {
      toUpperCase(text) {
        return text.toUpperCase();
      },
      ...mapMutations([
        'UPDATE_MODULE_CODE'
      ]),
      updateCode() {
        this.UPDATE_MODULE_CODE(this.code)
      }
    },
    computed: {
      checkModuleCode() {
        // this.$store.commit('updateCode', this.code)
        if (this.code.length == 0) {
          return 'null'
        }
        else {
          let mod = this.code.toUpperCase()
          if (this.modulelist.includes(mod)){ //this.code
            this.isInvalidInput = false
            return true
          }
          else{
            this.isInvalidInput = true
            return false
          }
        }
      },
      isInvalidInputR(){
        /**return ''**/
        if (this.isInvalidInput) {
          return ''
        }
        else {
          return 'click'
        }
      }
    },
    name: "home",
    components: {
      Footer
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.categoryHeader {
  color: #003d7c;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "bold"; /**330;**/
  font-size: 27px; /**32px;**/
  width: 100%;
  text-align: center;
  margin-bottom: 30px;
  margin-top: 30px;
}

.cardTitle1, .cardTitle2, .cardTitle3{
  color: #424242;
  font-weight: bold; /**bold or "200"**/
  font-size: 20px;
  margin-top: -10px;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  text-decoration:none !important;
}

.cardTitle1:hover,.cardTitle2:hover,.cardTitle3:hover {
  transition: all 1s ease-in-out;
  text-decoration: none!important;
  color:#3AAFA9;
  box-shadow: 0px 0px 0px 2px #3AAFA9;
}
a:hover{
  text-decoration:none !important;
}
button {
  background: #262626;
  height: 38px;
  /**
  border-radius: 2px;
  border: #fff; none
  color: #fff;
  text-emphasis-color: #E27979;
  padding: 10px;
  margin: 5px;**/
}

.buttontext {
  color: #F9F9F9;
  /**font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;**/
  font-weight: "bold"; /**330;**/
  font-size: 14px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

</style>
