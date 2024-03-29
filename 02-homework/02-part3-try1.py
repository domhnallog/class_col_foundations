###  Domhnall O'Donnchadha
###  20190530
###  Homework 2, Part 3

import json

data = json.loads("{\"tracks\":[{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1YxmW7DO2dM05gwMKTbr7l\"},\"href\":\"https://api.spotify.com/v1/albums/1YxmW7DO2dM05gwMKTbr7l\",\"id\":\"1YxmW7DO2dM05gwMKTbr7l\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Fake Love\",\"type\":\"album\",\"uri\":\"spotify:album:1YxmW7DO2dM05gwMKTbr7l\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":207813,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600333\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/6NMNgWgEAzde5M8U3lc6FN\"},\"href\":\"https://api.spotify.com/v1/tracks/6NMNgWgEAzde5M8U3lc6FN\",\"id\":\"6NMNgWgEAzde5M8U3lc6FN\",\"name\":\"Fake Love\",\"popularity\":90,\"preview_url\":\"https://p.scdn.co/mp3-preview/b1c79b52128cc45a962cb87ba5a616ea6a435356?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:6NMNgWgEAzde5M8U3lc6FN\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3tVQdUvClmAT7URs9V3rsp\"},\"href\":\"https://api.spotify.com/v1/artists/3tVQdUvClmAT7URs9V3rsp\",\"id\":\"3tVQdUvClmAT7URs9V3rsp\",\"name\":\"WizKid\",\"type\":\"artist\",\"uri\":\"spotify:artist:3tVQdUvClmAT7URs9V3rsp\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/77DAFfvm3O9zT5dIoG0eIO\"},\"href\":\"https://api.spotify.com/v1/artists/77DAFfvm3O9zT5dIoG0eIO\",\"id\":\"77DAFfvm3O9zT5dIoG0eIO\",\"name\":\"Kyla\",\"type\":\"artist\",\"uri\":\"spotify:artist:77DAFfvm3O9zT5dIoG0eIO\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":173986,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51600028\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/12VWzyPDBCc8fqeWCAfNwR\"},\"href\":\"https://api.spotify.com/v1/tracks/12VWzyPDBCc8fqeWCAfNwR\",\"id\":\"12VWzyPDBCc8fqeWCAfNwR\",\"name\":\"One Dance\",\"popularity\":84,\"preview_url\":\"https://p.scdn.co/mp3-preview/98f60b086bb1da2ca2e4c217331b8c8cc801358d?cid=null\",\"track_number\":12,\"type\":\"track\",\"uri\":\"spotify:track:12VWzyPDBCc8fqeWCAfNwR\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/2z3NlPY0n0gHJPCPqrzA6V\"},\"href\":\"https://api.spotify.com/v1/albums/2z3NlPY0n0gHJPCPqrzA6V\",\"id\":\"2z3NlPY0n0gHJPCPqrzA6V\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Sneakin’\",\"type\":\"album\",\"uri\":\"spotify:album:2z3NlPY0n0gHJPCPqrzA6V\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/1URnnhqYAYcrqrcwql10ft\"},\"href\":\"https://api.spotify.com/v1/artists/1URnnhqYAYcrqrcwql10ft\",\"id\":\"1URnnhqYAYcrqrcwql10ft\",\"name\":\"21 Savage\",\"type\":\"artist\",\"uri\":\"spotify:artist:1URnnhqYAYcrqrcwql10ft\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":251333,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600337\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4ckuS4Nj4FZ7i3Def3Br8W\"},\"href\":\"https://api.spotify.com/v1/tracks/4ckuS4Nj4FZ7i3Def3Br8W\",\"id\":\"4ckuS4Nj4FZ7i3Def3Br8W\",\"name\":\"Sneakin’\",\"popularity\":82,\"preview_url\":\"https://p.scdn.co/mp3-preview/4fa89ace286252c33a1ca0d36e7555d6a451a2db?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:4ckuS4Nj4FZ7i3Def3Br8W\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H\"},\"href\":\"https://api.spotify.com/v1/artists/5pKCCKE2ajJHZ9KAiaK11H\",\"id\":\"5pKCCKE2ajJHZ9KAiaK11H\",\"name\":\"Rihanna\",\"type\":\"artist\",\"uri\":\"spotify:artist:5pKCCKE2ajJHZ9KAiaK11H\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":263373,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600088\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/7fJtPlEZKxu6gvkfBFc5tW\"},\"href\":\"https://api.spotify.com/v1/tracks/7fJtPlEZKxu6gvkfBFc5tW\",\"id\":\"7fJtPlEZKxu6gvkfBFc5tW\",\"name\":\"Too Good\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/e702c76de627c3fb04da1bcbf6a8b53c3326a0cc?cid=null\",\"track_number\":16,\"type\":\"track\",\"uri\":\"spotify:track:7fJtPlEZKxu6gvkfBFc5tW\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":245226,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600080\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4CpKEkdGbOJV51cSvx7SoG\"},\"href\":\"https://api.spotify.com/v1/tracks/4CpKEkdGbOJV51cSvx7SoG\",\"id\":\"4CpKEkdGbOJV51cSvx7SoG\",\"name\":\"Controlla\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/c5b5845dc83410f5731e395c5a725d6b6e94ff69?cid=null\",\"track_number\":11,\"type\":\"track\",\"uri\":\"spotify:track:4CpKEkdGbOJV51cSvx7SoG\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1ozpmkWcCHwsQ4QTnxOOdT\"},\"href\":\"https://api.spotify.com/v1/albums/1ozpmkWcCHwsQ4QTnxOOdT\",\"id\":\"1ozpmkWcCHwsQ4QTnxOOdT\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/77b0c91524867cc72d1974f66ad8cd21d063a20e\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/f2405b82d0578dd815a3082ca0f7ec4e18e937a1\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/a5435bb3ab4fabe43bc7f7ce46a6c23aa30d8eae\",\"width\":64}],\"name\":\"What A Time To Be Alive\",\"type\":\"album\",\"uri\":\"spotify:album:1ozpmkWcCHwsQ4QTnxOOdT\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":205879,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500300\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/27GmP9AWRs744SzKcpJsTZ\"},\"href\":\"https://api.spotify.com/v1/tracks/27GmP9AWRs744SzKcpJsTZ\",\"id\":\"27GmP9AWRs744SzKcpJsTZ\",\"name\":\"Jumpman\",\"popularity\":77,\"preview_url\":\"https://p.scdn.co/mp3-preview/4f3e954bb232a96c196389017d961016c8cbd7fc?cid=null\",\"track_number\":9,\"type\":\"track\",\"uri\":\"spotify:track:27GmP9AWRs744SzKcpJsTZ\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":267066,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51500238\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1OAYKfE0YdrN7C1yLWaLJo\"},\"href\":\"https://api.spotify.com/v1/tracks/1OAYKfE0YdrN7C1yLWaLJo\",\"id\":\"1OAYKfE0YdrN7C1yLWaLJo\",\"name\":\"Hotline Bling\",\"popularity\":75,\"preview_url\":\"https://p.scdn.co/mp3-preview/53a8f039eb0b567e47868f5a53de4683ba5d5f0c?cid=null\",\"track_number\":20,\"type\":\"track\",\"uri\":\"spotify:track:1OAYKfE0YdrN7C1yLWaLJo\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":189853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600078\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4YJmZfvlheSziXem8HBWrj\"},\"href\":\"https://api.spotify.com/v1/tracks/4YJmZfvlheSziXem8HBWrj\",\"id\":\"4YJmZfvlheSziXem8HBWrj\",\"name\":\"Still Here\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/39384d3485d21184dd3719cfd8d644182b0b1d8b?cid=null\",\"track_number\":10,\"type\":\"track\",\"uri\":\"spotify:track:4YJmZfvlheSziXem8HBWrj\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/79qV4McLzhs8U3FyRKnocz\"},\"href\":\"https://api.spotify.com/v1/albums/79qV4McLzhs8U3FyRKnocz\",\"id\":\"79qV4McLzhs8U3FyRKnocz\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/2151a609fd5a5ec69586920a85bf308cdf56f3a1\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/9c6eb30ff5270c115b1ecd2b74430e505c281f25\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/ef4e90b4dde72134365a732659dccf9e1bd7b519\",\"width\":64}],\"name\":\"Back To Back\",\"type\":\"album\",\"uri\":\"spotify:album:79qV4McLzhs8U3FyRKnocz\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":170637,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500241\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/5lFDtgWsjRJu8fPOAyJIAK\"},\"href\":\"https://api.spotify.com/v1/tracks/5lFDtgWsjRJu8fPOAyJIAK\",\"id\":\"5lFDtgWsjRJu8fPOAyJIAK\",\"name\":\"Back To Back\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/b5bb11586af5cfde7c0eaef26300b2f6f62d2ac4?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:5lFDtgWsjRJu8fPOAyJIAK\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0ptlfJfwGTy0Yvrk14JK1I\"},\"href\":\"https://api.spotify.com/v1/albums/0ptlfJfwGTy0Yvrk14JK1I\",\"id\":\"0ptlfJfwGTy0Yvrk14JK1I\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/d329671363eb7826b5871eef978841c7db97c757\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/bcd6801c26cb293a45df9b092227395c5b403b4c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/14d65d4565838431345e35575b8b74d95134990a\",\"width\":64}],\"name\":\"If You're Reading This It's Too Late\",\"type\":\"album\",\"uri\":\"spotify:album:0ptlfJfwGTy0Yvrk14JK1I\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":241853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500010\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1ID1QFSNNxi0hiZCNcwjUC\"},\"href\":\"https://api.spotify.com/v1/tracks/1ID1QFSNNxi0hiZCNcwjUC\",\"id\":\"1ID1QFSNNxi0hiZCNcwjUC\",\"name\":\"Legend\",\"popularity\":72,\"preview_url\":\"https://p.scdn.co/mp3-preview/34fe00d7d951e42017bbbd8a424244c3cf1006e1?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:1ID1QFSNNxi0hiZCNcwjUC\"}]}")



# print(type(data))               #type is dictionary
# print(data.keys())              #only content is 'tracks'

# trax = data['tracks']
# print(type(trax))               #type is list
# print(len(trax))                #contains 10 elements
# print(trax)
# for trak in trax:
#     print(trak, type(trak))
#     print(trak.keys())

# for trak in trax:
#   print(trak)

# print("0", type(data['tracks'][0]))
# print("1", type(data['tracks'][1]))
# print("2", type(data['tracks'][2]))
# print("3", type(data['tracks'][3]))
# print("4", type(data['tracks'][4]))
# print("5", type(data['tracks'][5]))
# print("6", type(data['tracks'][6]))
# print("7", type(data['tracks'][7]))
# print("8", type(data['tracks'][8]))
# print("9", type(data['tracks'][9]))

# print("0", data['tracks'][0].keys())
# print("1", data['tracks'][1].keys())
# print("2", data['tracks'][2].keys())
# print("3", data['tracks'][3].keys())
# print("4", data['tracks'][4].keys())
# print("5", data['tracks'][5].keys())
# print("6", data['tracks'][6].keys())
# print("7", data['tracks'][7].keys())
# print("8", data['tracks'][8].keys())
# print("9", data['tracks'][9].keys())

### 'album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri'

# print("album", type(data['tracks'][0]['album']))                          #dict
# print("album_name", type(data['tracks'][0]['album']['name']))             #str
# print("album_artists", type(data['tracks'][0]['album']['artists']))       #list
print("album_artists", type(data['tracks'][0]['album']['artists']['name']))       #list
# print("album_type", type(data['tracks'][0]['album']['type']))             #str
# print("artists", type(data['tracks'][0]['artists'][0]['name']))           #list
# print("available_markets", type(data['tracks'][0]['available_markets']))  #list
# print("disc_number", type(data['tracks'][0]['disc_number']))              #int
# print("duration_ms", type(data['tracks'][0]['duration_ms']))              #int
# print("explicit", type(data['tracks'][0]['explicit']))                    #bool
# print("external_ids", type(data['tracks'][0]['external_ids']))            #dict
# print("external_urls", type(data['tracks'][0]['external_urls']))          #dict
# print("href", type(data['tracks'][0]['href']))                            #str
# print("id", type(data['tracks'][0]['id']))                                #str
# print("name", type(data['tracks'][0]['name']))                            #str
# print("popularity", type(data['tracks'][0]['popularity']))                #int
# print("preview_url", type(data['tracks'][0]['preview_url']))              #str
# print("track_number", type(data['tracks'][0]['track_number']))            #int
# print("type", type(data['tracks'][0]['type']))                            #str
# print("uri", type(data['tracks'][0]['uri']))                              #str


# trx_album = data['tracks'][0]['album']                      #dict
trx_album = data['tracks'][0]['album']['name']              #dict
trx_albumartists = data['tracks'][0]['album']['artists']['name']    #list
trx_type = data['tracks'][0]['album']['type']               #str
trx_artists = data['tracks'][0]['artists'][0]['name']       #str
trx_markets = data['tracks'][0]['available_markets']        #list
trx_discnum = data['tracks'][0]['disc_number']              #int
trx_duration = data['tracks'][0]['duration_ms']             #int
trx_explicit = data['tracks'][0]['explicit']                #bool
trx_ext_ids = data['tracks'][0]['external_ids']             #dict
trx_ext_url = data['tracks'][0]['external_urls']            #dict
trx_href = data['tracks'][0]['href']                        #str
trx_id = data['tracks'][0]['id']                            #str
trx_name = data['tracks'][0]['name']                        #str
trx_popularity = data['tracks'][0]['popularity']            #int
trx_prev_url = data['tracks'][0]['preview_url']             #str
trx_tracknum = data['tracks'][0]['track_number']            #int
trx_type = data['tracks'][0]['type']                        #str
trx_uri = data['tracks'][0]['uri']                          #str


print("trx_album", trx_album)
print("trx_albumartists", trx_albumartists)
print("trx_type", trx_type)
print("trx_artists", trx_artists)
print("trx_markets", trx_markets)
print("trx_discnum", trx_discnum)
print("trx_duration", trx_duration)
print("trx_explicit", trx_explicit)
print("trx_ext_ids", trx_ext_ids.keys())
print("trx_ext_url", trx_ext_url.keys())
print("trx_href", trx_href)
print("trx_id", trx_id)
print("trx_name", trx_name)
print("trx_popularity", trx_popularity)
print("trx_prev_url", trx_prev_url)
print("trx_tracknum", trx_tracknum)
print("trx_type", trx_type)
print("trx_uri", trx_uri)


# print("0", data['tracks'][0]['artists'])
# print("1", data['tracks'][1]['artists'])
# print("2", data['tracks'][2]['artists'])
# print("3", data['tracks'][3]['artists'])
# print("4", data['tracks'][4]['artists'])
# print("5", data['tracks'][5]['artists'])
# print("6", data['tracks'][6]['artists'])
# print("7", data['tracks'][7]['artists'])
# print("8", data['tracks'][8]['artists'])
# print("9", data['tracks'][9]['artists'])


# print("0", data['tracks'][0]['album'])
# print("1", data['tracks'][1]['album'])
# print("2", data['tracks'][2]['album'])
# print("3", data['tracks'][3]['album'])
# print("4", data['tracks'][4]['album'])
# print("5", data['tracks'][5]['album'])
# print("6", data['tracks'][6]['album'])
# print("7", data['tracks'][7]['album'])
# print("8", data['tracks'][8]['album'])
# print("9", data['tracks'][9]['album'])

#print("0", data['tracks'][0]['album'].keys())

### 'album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'type', 'uri'

# print("0", data['tracks'][0]['album']['name'])
# print("0", data['tracks'][1]['album']['name'])
# print("0", data['tracks'][3]['album']['name'])
# print("0", data['tracks'][8]['album']['name'])

# print("2", data['tracks'][0]['album']['name'])
# print("2", data['tracks'][1]['album']['name'])
# print("2", data['tracks'][3]['album']['name'])
# print("2", data['tracks'][8]['album']['name'])

# print("4", data['tracks'][0]['album']['name'])
# print("4", data['tracks'][1]['album']['name'])
# print("4", data['tracks'][3]['album']['name'])
# print("4", data['tracks'][8]['album']['name'])




# 1. How many songs are there?

# 2. List the name of each song, along with its popularity.

# 3. How long would it take, in minutes, to listen to all of these songs in a row?

# 4. For each song, list every artist that worked on it.

# 5. For each song, list every musician that worked on it EXCEPT drake

# 6. How many songs are from albums, and how many are from singles?

# 7. What percentage of these songs are marked as explicit?

# 8. I'd like to listen to one of the songs! Is there maybe a URL where I can listen to it?

# 9. What is the most popular song?



###
# trx_album = data['tracks'][1]['album']['name']              #dict
# trx_albumartists = data['tracks'][1]['album']['artists']    #list
# trx_type = data['tracks'][1]['album']['type']               #str
# trx_artists = data['tracks'][1]['artists'][0]['name']       #str
# trx_markets = data['tracks'][1]['available_markets']        #list
# trx_discnum = data['tracks'][1]['disc_number']              #int
# trx_duration = data['tracks'][1]['duration_ms']             #int
# trx_explicit = data['tracks'][1]['explicit']                #bool
# trx_ext_ids = data['tracks'][1]['external_ids']             #dict
# trx_ext_url = data['tracks'][1]['external_urls']            #dict
# trx_href = data['tracks'][1]['href']                        #str
# trx_id = data['tracks'][1]['id']                            #str
# trx_name = data['tracks'][1]['name']                        #str
# trx_popularity = data['tracks'][1]['popularity']            #int
# trx_prev_url = data['tracks'][1]['preview_url']             #str
# trx_tracknum = data['tracks'][1]['track_number']            #int
# trx_type = data['tracks'][1]['type']                        #str
# trx_uri = data['tracks'][1]['uri']                          #str

# print("trx_album", trx_album)
# print("trx_albumartists", trx_albumartists)
# print("trx_type", trx_type)
# print("trx_artists", trx_artists)
# print("trx_markets", trx_markets)
# print("trx_discnum", trx_discnum)
# print("trx_duration", trx_duration)
# print("trx_explicit", trx_explicit)
# print("trx_ext_ids", trx_ext_ids.keys())
# print("trx_ext_url", trx_ext_url.keys())
# print("trx_href", trx_href)
# print("trx_id", trx_id)
# print("trx_name", trx_name)
# print("trx_popularity", trx_popularity)
# print("trx_prev_url", trx_prev_url)
# print("trx_tracknum", trx_tracknum)
# print("trx_type", trx_type)
# print("trx_uri", trx_uri)



# trx_album = data['tracks'][2]['album']['name']              #dict
# trx_albumartists = data['tracks'][2]['album']['artists']    #list
# trx_type = data['tracks'][2]['album']['type']               #str
# trx_artists = data['tracks'][2]['artists'][0]['name']       #str
# trx_markets = data['tracks'][2]['available_markets']        #list
# trx_discnum = data['tracks'][2]['disc_number']              #int
# trx_duration = data['tracks'][2]['duration_ms']             #int
# trx_explicit = data['tracks'][2]['explicit']                #bool
# trx_ext_ids = data['tracks'][2]['external_ids']             #dict
# trx_ext_url = data['tracks'][2]['external_urls']            #dict
# trx_href = data['tracks'][2]['href']                        #str
# trx_id = data['tracks'][2]['id']                            #str
# trx_name = data['tracks'][2]['name']                        #str
# trx_popularity = data['tracks'][2]['popularity']            #int
# trx_prev_url = data['tracks'][2]['preview_url']             #str
# trx_tracknum = data['tracks'][2]['track_number']            #int
# trx_type = data['tracks'][2]['type']                        #str
# trx_uri = data['tracks'][2]['uri']                          #str

# print("trx_album", trx_album)
# print("trx_albumartists", trx_albumartists)
# print("trx_type", trx_type)
# print("trx_artists", trx_artists)
# print("trx_markets", trx_markets)
# print("trx_discnum", trx_discnum)
# print("trx_duration", trx_duration)
# print("trx_explicit", trx_explicit)
# print("trx_ext_ids", trx_ext_ids.keys())
# print("trx_ext_url", trx_ext_url.keys())
# print("trx_href", trx_href)
# print("trx_id", trx_id)
# print("trx_name", trx_name)
# print("trx_popularity", trx_popularity)
# print("trx_prev_url", trx_prev_url)
# print("trx_tracknum", trx_tracknum)
# print("trx_type", trx_type)
# print("trx_uri", trx_uri)



# trx_album = data['tracks'][3]['album']['name']              #dict
# trx_albumartists = data['tracks'][3]['album']['artists']    #list
# trx_type = data['tracks'][3]['album']['type']               #str
# trx_artists = data['tracks'][3]['artists'][0]['name']       #str
# trx_markets = data['tracks'][3]['available_markets']        #list
# trx_discnum = data['tracks'][3]['disc_number']              #int
# trx_duration = data['tracks'][3]['duration_ms']             #int
# trx_explicit = data['tracks'][3]['explicit']                #bool
# trx_ext_ids = data['tracks'][3]['external_ids']             #dict
# trx_ext_url = data['tracks'][3]['external_urls']            #dict
# trx_href = data['tracks'][3]['href']                        #str
# trx_id = data['tracks'][3]['id']                            #str
# trx_name = data['tracks'][3]['name']                        #str
# trx_popularity = data['tracks'][3]['popularity']            #int
# trx_prev_url = data['tracks'][3]['preview_url']             #str
# trx_tracknum = data['tracks'][3]['track_number']            #int
# trx_type = data['tracks'][3]['type']                        #str
# trx_uri = data['tracks'][3]['uri']                          #str

# print("trx_album", trx_album)
# print("trx_albumartists", trx_albumartists)
# print("trx_type", trx_type)
# print("trx_artists", trx_artists)
# print("trx_markets", trx_markets)
# print("trx_discnum", trx_discnum)
# print("trx_duration", trx_duration)
# print("trx_explicit", trx_explicit)
# print("trx_ext_ids", trx_ext_ids.keys())
# print("trx_ext_url", trx_ext_url.keys())
# print("trx_href", trx_href)
# print("trx_id", trx_id)
# print("trx_name", trx_name)
# print("trx_popularity", trx_popularity)
# print("trx_prev_url", trx_prev_url)
# print("trx_tracknum", trx_tracknum)
# print("trx_type", trx_type)
# print("trx_uri", trx_uri)



# trx_album = data['tracks'][4]['album']['name']              #dict
# trx_albumartists = data['tracks'][4]['album']['artists']    #list
# trx_type = data['tracks'][4]['album']['type']               #str
# trx_artists = data['tracks'][4]['artists'][0]['name']       #str
# trx_markets = data['tracks'][4]['available_markets']        #list
# trx_discnum = data['tracks'][4]['disc_number']              #int
# trx_duration = data['tracks'][4]['duration_ms']             #int
# trx_explicit = data['tracks'][4]['explicit']                #bool
# trx_ext_ids = data['tracks'][4]['external_ids']             #dict
# trx_ext_url = data['tracks'][4]['external_urls']            #dict
# trx_href = data['tracks'][4]['href']                        #str
# trx_id = data['tracks'][4]['id']                            #str
# trx_name = data['tracks'][4]['name']                        #str
# trx_popularity = data['tracks'][4]['popularity']            #int
# trx_prev_url = data['tracks'][4]['preview_url']             #str
# trx_tracknum = data['tracks'][4]['track_number']            #int
# trx_type = data['tracks'][4]['type']                        #str
# trx_uri = data['tracks'][4]['uri']                          #str

# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# print("trx_album", trx_album)
# print("trx_albumartists", trx_albumartists)
# print("trx_type", trx_type)
# print("trx_artists", trx_artists)
# print("trx_markets", trx_markets)
# print("trx_discnum", trx_discnum)
# print("trx_duration", trx_duration)
# print("trx_explicit", trx_explicit)
# print("trx_name", trx_name)
# print("trx_popularity", trx_popularity)
# print("trx_tracknum", trx_tracknum)