# moe_count
Add a banner with cute girls to count visits!

![counter](https://count.kamuridesu.com/?username=moe_count)
# usage
Add this to your profile:
## Markdown
```md
![alt text](https://count.kamuridesu.tech?username=moe_count)
```
## HTML
```md
<img src=http://count.kamuridesu.tech?username=moe_count](http://count.kamuridesu.tech?username=moe_count/>
```
But instead of `moe_count` put your username or some unique identifier


# Self hosting
Build the container image:
```
docker build -t moe_count .
```

Run the container:
```
docker run --name moe_count -v $(pwd)/databases:/app/db --restart always -d -p 5003:80 moe_count
```
