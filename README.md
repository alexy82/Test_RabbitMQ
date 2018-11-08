# Message queue manager

 
## Exchange

> Cấu trúc config các exchange

 **Syntax Declare Exchange**
	


   ```python
   EXCHANGES = 
    {
        '_name_exchange_': {
            'type': '_type_exchange_',
            'config': {
                'passive': _boolean_,
                'durable': _boolean_,
                'auto_delete': _boolean_,
                'internal': _boolean_,
                'arguments': None,
            },
            'connection_type': 'settings' or 'url',
            'url': '_url_connection_'
            'settings': name connection in settings.py

        },
   ```
**Example**
	
```python
   EXCHANGES = \
    {
        'teko.test_exchange': {
            'type': 'topic',
            'config': {
                'passive': False,
                'durable': True,
                'auto_delete': False,
                'internal': False,
                'arguments': None,
            },
            'connection_type': 'setting',
            'setting': 'default'

        },
        }
```
**Syntax Bind Exchange**

```python
    EXCHANGES_BIND = {
    '_name_exchange_':
        [{
                'name': '_name_another_exchange_',
                'routing_key': '_routing_key_',
                'arguments': None,
            },]
	}
```
**Example**
```python

    EXCHANGES_BIND = {
    'teko.test_exchange':
        [
            {
                'name': 'exchange1',
                'routing_key': '*.*.*',
                'arguments': None,
            },
            {
                'name': 'exchange2',
                'routing_key': '*.*.*',
                'arguments': None,
            },

        ]}
```
**Yêu cầu**
 - File config bắt buộc phải là file python (.py)
 - Không được đặt tên file là settings.py
 - Đảm bảo là file có 2 dictionary là EXCHANGES VÀ EXCHANGES_BIND
 
 ## Queue
 > Cấu trúc config các queue
 
 **Syntax Declare Queue**
 ```python
    QUEUES = 
    {
        '_name_queue': {
            'config': {
                'passive': _boolean_,
                'durable': _boolean_,
                'exclusive': _boolean_,
                'auto_delete': _boolean,
                'arguments': None
            },
            'connection_type': 'settings' or 'url',
            'url': '_url_connection_',
            'settings': name connection in settings.py,
           },
    }
  ```
**Example**
	
```python
    QUEUES = \
    {
        'test': {
            'config': {
                'passive': False,
                'durable': False,
                'exclusive': False,
                'auto_delete': False,
                'arguments': None
            },
            'connection_type': 'url',
            'url': 'amqp://rzblafqf:ZnUhFd1ElXuzsUpUNsmgV-GmCpiQxqkz@woodpecker.rmq.cloudamqp.com/rzblafqf',

        },
        }
 ```

**Syntax Bind Queue**

```python
   EXCHANGES_BIND = {
    '_name_exchange_':
        [{
                'name': '_name_another_exchange_',
                'routing_key': '_routing_key_',
                'arguments': None,
            },]
	}
```
**Example**
```python
   EXCHANGES_BIND = {
    'teko.test_exchange':
        [
            {
                'name': 'exchange1',
                'routing_key': '*.*.*',
                'arguments': None,
            },
            {
                'name': 'exchange2',
                'routing_key': '*.*.*',
                'arguments': None,
            },

        ]}
  ```

**Yêu cầu**
 - File config bắt buộc phải là file python (.py)
 - Không được đặt tên file là settings.py
 - Đảm bảo là file có 2 dictionary là QUEUES Và QUEUES_BIND
 
 ## Declare exchange with command line
 

**Syntax**
```bash
python command/exchange.py -f <filename> -a <action> -e <exchange_name>
```

|       |Kiểu dữ liệu  | Giải thích |Mặc định |
|--------|-----| -----|-----|
|<pre>-f, --file</pre>     |String| đường dẫn 1 file config exchange khác (file python)  | file exchange_config.py trong hệ thống|
|<pre>-a, --action</pre>  |  String| chỉ được chọn:<br> **remove**: xóa exchange <br> **declare**: tạo exchange<br> **bind**: bind exchange      |  **declare** |
| <pre>-e, --exchange</pre>| String| tên exchange cụ thể thể thực hiện 1 action     |    tất cả exchange |

## Declare queue with command line
 

**Syntax**
```bash
python command/queue.py -f <filename> -a <action> -q <queue_name> -p <pattern> -e <if_empty> -u <if_unused>
```

|        | Kiểu dữ liệu | Giải thích |Mặc định |
|--------|-----| -----|-----|
|<pre>-f, --file</pre>    |String | đường dẫn 1 file config queue khác (file python) | file queue_config.py trong hệ thống|
|<pre>-a, --action</pre>    | String| chỉ được chọn:<br> **remove**: xóa queue  <br>**declare**: tạo queue<br> **bind**: bind queue <br> **purge**: purge queue     |  **declare** |
| <pre>-q, --queue</pre>|String | tên queue cụ thể thể thực hiện 1 action     |    tất cả queue |
|<pre>-p, --pattern</pre>|String|Pattern để thực hiện 1 action với các queue match với pattern<br> **Lưu ý** -q và -p không thể dùng chung|tất cả queue|
|<pre>-e, --empty</pre>|Boolean| if_empty chỉ dùng chung với action **remove** xóa các queue nếu queue đó không chưa message (rỗng)|False|
|<pre>-u, --unused</pre>|Boolean| if_unused chỉ dùng chung với action **remove** xóa các queue nếu không có consumer nào connect đến |False|



 
