<template>
  <div class="hello">
    <h1>Weather Report</h1>
    <div>
      The temperature will be: {{ temperature }} 
      and the chance of {{ precip_type }} is {{ precip_chance }}!
    </div>
  </div>
</template>

<script>

  import axios from "axios";

  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    },
    data() {
      return {
        temperature: 0,
        precip_type: 'rain',
        precip_chance: 80
      };
    },
    async mounted() {
      await axios({ method: "GET", "url": "http://localhost/temperature" })
          .then(result => {
            this.temperature = result.data['temperature_c'];
          }, error => {
            console.error(error);
          });

      await axios({ method: "GET", "url": `http://localhost/precipitation?temp=${this.temperature}` })
          .then(result => {
            this.precip_chance = result.data['precip_chance'];
            this.precip_type = result.data['type'];
          }, error => {
            console.error(error);
          });
    }
  }
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
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
