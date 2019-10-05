<template>
  <div class="main">
    <b-container fluid class="content">
      <b-row align-h="center">
        <b-col cols="12" class="moduleTitle">{{ code }}</b-col>
      </b-row>

      <b-row align-h="center">
        <b-col cols="12" class="moduleName">{{ name }}</b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
//Have to import json data or wherever is our individual module data source
//e.g. import json_data from './indiv-mod-data.json'

export default {
  name: 'ModuleTitle',
  props: {
    code: String,
    name: String
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.moduleTitle {
  color: #FF5138;
  font-family: sans-serif;
  font-weight: "bold"; /**330;**/
  font-size: 50px;
  width: 100%;
  text-align: center;
  margin-top: 60px;
  padding-bottom: 0px;
  text-transform: uppercase;
  font-weight:600;
  /**margin: 10px auto 10px;**/
}

.moduleName {
  color: grey;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "200";
  font-size: 20px;
  width: 100%;
  text-align: center;
  margin-top: -14px;
  /**margin: 10px auto 10px;**/
}

/** Not Used
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
**/
</style>
