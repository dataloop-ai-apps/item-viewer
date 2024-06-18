cp /tmp/app/nginx.conf /etc/nginx/conf.d
#npm run dev &
#python -m uvicorn "functions.app:app" \
#        --reload \
#        --host="0.0.0.0" \
#        --port=5463 \
#        --timeout-keep-alive=60 \
#        2>&1 | tee output.log &

nginx
tail -f /tmp/error.log
