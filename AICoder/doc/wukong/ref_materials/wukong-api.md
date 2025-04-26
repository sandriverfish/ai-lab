# 悟空终端 API

# TerminalController

# bind

绑定终端

根据终端绑定请求参数进行绑定

```
/api/terminal/bind
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-bind-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/bind"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalBindReqDTO body = ; // TerminalBindReqDTO |
        try {
            ResultTerminalBindRespDTO result = apiInstance.bind(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#bind");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalBindReqDTO body = ; // TerminalBindReqDTO |
        try {
            ResultTerminalBindRespDTO result = apiInstance.bind(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#bind");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalBindReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 绑定终端
[apiInstance bindWith:body\
              completionHandler: ^(ResultTerminalBindRespDTO output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalBindReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.bind(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class bindExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalBindReqDTO(); // TerminalBindReqDTO |

            try
            {
                // 绑定终端
                ResultTerminalBindRespDTO result = apiInstance.bind(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.bind: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalBindReqDTO |

try {
    $result = $api_instance->bind($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->bind: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalBindReqDTO->new(); # TerminalBindReqDTO |

eval {
    my $result = $api_instance->bind(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->bind: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalBindReqDTO |

try:
    # 绑定终端
    api_response = api_instance.bind(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->bind: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端绑定请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>} |

## Responses

### Status: 200 - 成功绑定终端

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-bind-200-schema)

{

code:

integer(int32)

message:

string

data:

{

终端绑定响应参数

terminalCode:

string

终端编码

hardwareCode:

string

硬件编码

}

}

* * *

# getConfigs

获取终端配置列表

获取终端配置列表

```
/api/terminal/configs
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getConfigs-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/configs"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalCommonReqDTO body = ; // TerminalCommonReqDTO |
        try {
            ResultTerminalGetConfigsRespDTO result = apiInstance.getConfigs(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#getConfigs");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalCommonReqDTO body = ; // TerminalCommonReqDTO |
        try {
            ResultTerminalGetConfigsRespDTO result = apiInstance.getConfigs(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#getConfigs");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalCommonReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 获取终端配置列表
[apiInstance getConfigsWith:body\
              completionHandler: ^(ResultTerminalGetConfigsRespDTO output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalCommonReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getConfigs(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class getConfigsExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalCommonReqDTO(); // TerminalCommonReqDTO |

            try
            {
                // 获取终端配置列表
                ResultTerminalGetConfigsRespDTO result = apiInstance.getConfigs(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.getConfigs: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalCommonReqDTO |

try {
    $result = $api_instance->getConfigs($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->getConfigs: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalCommonReqDTO->new(); # TerminalCommonReqDTO |

eval {
    my $result = $api_instance->getConfigs(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->getConfigs: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalCommonReqDTO |

try:
    # 获取终端配置列表
    api_response = api_instance.get_configs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->getConfigs: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端通用请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>} |

## Responses

### Status: 200 - 成功获取终端配置列表

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-getConfigs-200-schema)

{

code:

integer(int32)

message:

string

data:

{

获取终端配置列表

terminalCode:

string

终端编码

configs:

\[\
\
配置列表\
\
{\
\
配置\
\
id:\
\
integer(int32)\
\
ID\
\
configKey:\
\
string\
\
配置项，示例：app.pollingInterval、app.ntpServer、app.i18nLanguage、app.jobSoundEffect\
\
configValue:\
\
string\
\
配置值，具体取值说明：\
\
- app.pollingInterval: 轮询间隔，单位为秒，例如 '10'。\
- app.ntpServer: NTP 服务器地址，例如 'ntp.ntsc.ac.cn' 或 '0.cn.pool.ntp.org'。\
- app.i18nLanguage: 国际化语言，例如 'zh-CN', 'en-US', 'th-TH'。\
- app.jobSoundEffect: 作业音效设置，取值包括 'SILENT'（不提示）、'GENTLE'（轻柔音效）、'STANDARD'（标准音效）、'LOUD'（响亮音效）。\
\
seq:\
\
integer(int32)\
\
排序\
\
}\
\
\]

}

}

* * *

# getLatestAppVersion

获取终端最新App版本

获取终端最新App版本

```
/api/terminal/latest-app-version
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getLatestAppVersion-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/latest-app-version"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalGetLatestAppVersionReqDTO body = ; // TerminalGetLatestAppVersionReqDTO |
        try {
            ResultTerminalGetLatestAppVersionRespDTO result = apiInstance.getLatestAppVersion(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#getLatestAppVersion");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalGetLatestAppVersionReqDTO body = ; // TerminalGetLatestAppVersionReqDTO |
        try {
            ResultTerminalGetLatestAppVersionRespDTO result = apiInstance.getLatestAppVersion(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#getLatestAppVersion");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalGetLatestAppVersionReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 获取终端最新App版本
[apiInstance getLatestAppVersionWith:body\
              completionHandler: ^(ResultTerminalGetLatestAppVersionRespDTO output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalGetLatestAppVersionReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getLatestAppVersion(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class getLatestAppVersionExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalGetLatestAppVersionReqDTO(); // TerminalGetLatestAppVersionReqDTO |

            try
            {
                // 获取终端最新App版本
                ResultTerminalGetLatestAppVersionRespDTO result = apiInstance.getLatestAppVersion(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.getLatestAppVersion: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalGetLatestAppVersionReqDTO |

try {
    $result = $api_instance->getLatestAppVersion($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->getLatestAppVersion: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalGetLatestAppVersionReqDTO->new(); # TerminalGetLatestAppVersionReqDTO |

eval {
    my $result = $api_instance->getLatestAppVersion(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->getLatestAppVersion: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalGetLatestAppVersionReqDTO |

try:
    # 获取终端最新App版本
    api_response = api_instance.get_latest_app_version(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->getLatestAppVersion: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端通用请求参数<br>Required: versionName<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>versionName:<br>string<br>版本名称<br>} |

## Responses

### Status: 200 - 成功获取终端最新App版本

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-getLatestAppVersion-200-schema)

{

code:

integer(int32)

message:

string

data:

{

获取终端最新App版本

appVersion:

{

APP版本

id:

integer

versionName:

string

versionNumber:

integer

file:

string

fileName:

string

fileSize:

integer

checksum:

string

createdAt:

string

updatedAt:

string

}

}

}

* * *

# getSchedules

获取终端定时任务列表

获取终端定时任务列表

```
/api/terminal/schedules
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-getSchedules-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/schedules"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalCommonReqDTO body = ; // TerminalCommonReqDTO |
        try {
            ResultTerminalGetSchedulesRespDTO result = apiInstance.getSchedules(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#getSchedules");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalCommonReqDTO body = ; // TerminalCommonReqDTO |
        try {
            ResultTerminalGetSchedulesRespDTO result = apiInstance.getSchedules(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#getSchedules");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalCommonReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 获取终端定时任务列表
[apiInstance getSchedulesWith:body\
              completionHandler: ^(ResultTerminalGetSchedulesRespDTO output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalCommonReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getSchedules(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class getSchedulesExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalCommonReqDTO(); // TerminalCommonReqDTO |

            try
            {
                // 获取终端定时任务列表
                ResultTerminalGetSchedulesRespDTO result = apiInstance.getSchedules(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.getSchedules: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalCommonReqDTO |

try {
    $result = $api_instance->getSchedules($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->getSchedules: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalCommonReqDTO->new(); # TerminalCommonReqDTO |

eval {
    my $result = $api_instance->getSchedules(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->getSchedules: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalCommonReqDTO |

try:
    # 获取终端定时任务列表
    api_response = api_instance.get_schedules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->getSchedules: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端通用请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>} |

## Responses

### Status: 200 - 成功获取终端定时任务列表

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-getSchedules-200-schema)

{

code:

integer(int32)

message:

string

data:

{

获取终端定时任务列表

terminalCode:

string

终端编码

schedules:

\[\
\
定时任务列表\
\
{\
\
设备定时任务\
\
id:\
\
integer(int32)\
\
ID\
\
deviceId:\
\
integer(int32)\
\
所属终端\
\
taskType:\
\
string\
\
任务类型\
\
**Enum:** `POWER_ON`, `POWER_OFF`\
\
taskTime:\
\
string\
\
任务时间\
\
daysOfWeek:\
\
string\
\
任务执行的星期几\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deviceName:\
\
string\
\
终端名称\
\
terminalCode:\
\
string\
\
终端编码\
\
hardwareCode:\
\
string\
\
硬件编码\
\
}\
\
\]

}

}

* * *

# init

初始化终端

根据终端初始化请求参数进行初始化

```
/api/terminal/init
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-init-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/init"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalInitReqDTO body = ; // TerminalInitReqDTO |
        try {
            ResultTerminalInitRespDTO result = apiInstance.init(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#init");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalInitReqDTO body = ; // TerminalInitReqDTO |
        try {
            ResultTerminalInitRespDTO result = apiInstance.init(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#init");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalInitReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 初始化终端
[apiInstance initWith:body\
              completionHandler: ^(ResultTerminalInitRespDTO output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalInitReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.init(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class initExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalInitReqDTO(); // TerminalInitReqDTO |

            try
            {
                // 初始化终端
                ResultTerminalInitRespDTO result = apiInstance.init(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.init: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalInitReqDTO |

try {
    $result = $api_instance->init($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->init: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalInitReqDTO->new(); # TerminalInitReqDTO |

eval {
    my $result = $api_instance->init(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->init: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalInitReqDTO |

try:
    # 初始化终端
    api_response = api_instance.init(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->init: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端初始化请求参数<br>Required: hardwareCode<br>hardwareCode:<br>string<br>硬件编码<br>ipAddress:<br>string<br>IP 地址<br>macAddress:<br>string<br>MAC 地址<br>versionName:<br>string<br>版本名称<br>versionNumber:<br>string<br>版本号<br>manufacturer:<br>string<br>制造商<br>model:<br>string<br>型号<br>} |

## Responses

### Status: 200 - 成功初始化终端

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-init-200-schema)

{

code:

integer(int32)

message:

string

data:

{

终端初始化响应参数

terminalCode:

string

终端编码

name:

string

终端名称

timestamp:

integer(int64)

时间戳

configs:

\[\
\
配置列表\
\
{\
\
配置\
\
id:\
\
integer(int32)\
\
ID\
\
configKey:\
\
string\
\
配置项，示例：app.pollingInterval、app.ntpServer、app.i18nLanguage、app.jobSoundEffect\
\
configValue:\
\
string\
\
配置值，具体取值说明：\
\
- app.pollingInterval: 轮询间隔，单位为秒，例如 '10'。\
- app.ntpServer: NTP 服务器地址，例如 'ntp.ntsc.ac.cn' 或 '0.cn.pool.ntp.org'。\
- app.i18nLanguage: 国际化语言，例如 'zh-CN', 'en-US', 'th-TH'。\
- app.jobSoundEffect: 作业音效设置，取值包括 'SILENT'（不提示）、'GENTLE'（轻柔音效）、'STANDARD'（标准音效）、'LOUD'（响亮音效）。\
\
seq:\
\
integer(int32)\
\
排序\
\
}\
\
\]

schedules:

\[\
\
定时任务列表\
\
{\
\
设备定时任务\
\
id:\
\
integer(int32)\
\
ID\
\
deviceId:\
\
integer(int32)\
\
所属终端\
\
taskType:\
\
string\
\
任务类型\
\
**Enum:** `POWER_ON`, `POWER_OFF`\
\
taskTime:\
\
string\
\
任务时间\
\
daysOfWeek:\
\
string\
\
任务执行的星期几\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deviceName:\
\
string\
\
终端名称\
\
terminalCode:\
\
string\
\
终端编码\
\
hardwareCode:\
\
string\
\
硬件编码\
\
}\
\
\]

jobProcesses:

\[\
\
作业流程列表\
\
{\
\
作业流程\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
version:\
\
integer(int32)\
\
版本\
\
name:\
\
string\
\
作业流程名称\
\
deviceId:\
\
integer(int32)\
\
所属终端\
\
deviceUuid:\
\
string\
\
所属终端唯一标识\
\
autoLoop:\
\
integer(int32)\
\
是否自动循环（0: 否, 1: 是）\
\
ngTerminate:\
\
integer(int32)\
\
NG是否终止（0: 否, 1: 是）\
\
isDefault:\
\
integer(int32)\
\
是否默认作业流程（0: 否, 1: 是）\
\
isPublished:\
\
integer(int32)\
\
是否已发布（0: 否, 1: 是）\
\
creatorId:\
\
integer(int32)\
\
创建者ID\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
publishedAt:\
\
string(date-time)\
\
发布时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
deviceName:\
\
string\
\
终端名称\
\
terminalCode:\
\
string\
\
终端编码\
\
hardwareCode:\
\
string\
\
硬件编码\
\
jobInstructions:\
\
\[\
\
作业指示列表\
\
{\
\
作业指示\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
instructionText:\
\
string\
\
作业指示文本\
\
instructionImage:\
\
string\
\
作业指示图像（存储图像路径）\
\
instructionImageSize:\
\
integer(int64)\
\
图像大小（单位：字节）\
\
instructionImageChecksum:\
\
string\
\
图像校验值（如MD5）\
\
instructionThumbnail:\
\
string\
\
作业指示缩略图（存储缩略图路径）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
jobItems:\
\
\[\
\
作业项列表\
\
{\
\
作业项\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobInstructionId:\
\
integer(int32)\
\
所属作业指示\
\
jobInstructionUuid:\
\
string\
\
所属作业指示唯一标识\
\
itemImage:\
\
string\
\
作业项目图像\
\
itemImageSize:\
\
integer(int64)\
\
图像大小（单位：字节）\
\
itemImageChecksum:\
\
string\
\
图像校验值（如MD5）\
\
itemThumbnail:\
\
string\
\
作业项目缩略图\
\
mode:\
\
string\
\
模式（匹配模式，其他模式）\
\
standardTime:\
\
integer(int32)\
\
标准时间（单位：秒）\
\
upperLimitTime:\
\
integer(int32)\
\
上限时间（单位：秒）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
deviceScreenshotId:\
\
integer(int32)\
\
主图像Id\
\
baseSearchArea:\
\
{\
\
校验点\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobItemId:\
\
integer(int32)\
\
所属作业项目\
\
jobItemUuid:\
\
string\
\
所属作业项目唯一标识\
\
type:\
\
string\
\
类型：'BASE\_POINT', 'CHECK\_POINT', 'BASE\_SEARCH\_AREA'\
\
**Enum:** `BASE_POINT`, `CHECK_POINT`, `BASE_SEARCH_AREA`\
\
shape:\
\
string\
\
形状：'RECTANGLE', 'POLYGON'\
\
**Enum:** `RECTANGLE`, `POLYGON`\
\
left:\
\
integer(int32)\
\
左上角x坐标\
\
top:\
\
integer(int32)\
\
左上角y坐标\
\
width:\
\
integer(int32)\
\
矩形框的宽度\
\
height:\
\
integer(int32)\
\
矩形框的高度\
\
snapshot:\
\
string\
\
截图\
\
snapshotSize:\
\
integer(int64)\
\
图片大小（单位：字节）\
\
snapshotChecksum:\
\
string\
\
图片校验值（如MD5）\
\
snapshotBase64:\
\
string\
\
截图Base64，只用于前端传入\
\
similarity:\
\
number(double)\
\
相似度（范围0.50-1.00）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
unpublishedSnapshotPath:\
\
string\
\
未发布截图路径\
\
}\
\
basePoint:\
\
{\
\
校验点\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobItemId:\
\
integer(int32)\
\
所属作业项目\
\
jobItemUuid:\
\
string\
\
所属作业项目唯一标识\
\
type:\
\
string\
\
类型：'BASE\_POINT', 'CHECK\_POINT', 'BASE\_SEARCH\_AREA'\
\
**Enum:** `BASE_POINT`, `CHECK_POINT`, `BASE_SEARCH_AREA`\
\
shape:\
\
string\
\
形状：'RECTANGLE', 'POLYGON'\
\
**Enum:** `RECTANGLE`, `POLYGON`\
\
left:\
\
integer(int32)\
\
左上角x坐标\
\
top:\
\
integer(int32)\
\
左上角y坐标\
\
width:\
\
integer(int32)\
\
矩形框的宽度\
\
height:\
\
integer(int32)\
\
矩形框的高度\
\
snapshot:\
\
string\
\
截图\
\
snapshotSize:\
\
integer(int64)\
\
图片大小（单位：字节）\
\
snapshotChecksum:\
\
string\
\
图片校验值（如MD5）\
\
snapshotBase64:\
\
string\
\
截图Base64，只用于前端传入\
\
similarity:\
\
number(double)\
\
相似度（范围0.50-1.00）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
unpublishedSnapshotPath:\
\
string\
\
未发布截图路径\
\
}\
\
checkPoints:\
\
\[\
\
校验点列表\
\
{\
\
校验点\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobItemId:\
\
integer(int32)\
\
所属作业项目\
\
jobItemUuid:\
\
string\
\
所属作业项目唯一标识\
\
type:\
\
string\
\
类型：'BASE\_POINT', 'CHECK\_POINT', 'BASE\_SEARCH\_AREA'\
\
**Enum:** `BASE_POINT`, `CHECK_POINT`, `BASE_SEARCH_AREA`\
\
shape:\
\
string\
\
形状：'RECTANGLE', 'POLYGON'\
\
**Enum:** `RECTANGLE`, `POLYGON`\
\
left:\
\
integer(int32)\
\
左上角x坐标\
\
top:\
\
integer(int32)\
\
左上角y坐标\
\
width:\
\
integer(int32)\
\
矩形框的宽度\
\
height:\
\
integer(int32)\
\
矩形框的高度\
\
snapshot:\
\
string\
\
截图\
\
snapshotSize:\
\
integer(int64)\
\
图片大小（单位：字节）\
\
snapshotChecksum:\
\
string\
\
图片校验值（如MD5）\
\
snapshotBase64:\
\
string\
\
截图Base64，只用于前端传入\
\
similarity:\
\
number(double)\
\
相似度（范围0.50-1.00）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
unpublishedSnapshotPath:\
\
string\
\
未发布截图路径\
\
}\
\
\]\
\
unpublishedItemImagePath:\
\
string\
\
未发布作业项图像路径\
\
unpublishedItemThumbnailPath:\
\
string\
\
未发布作业项缩略图路径\
\
}\
\
\]\
\
unpublishedInstructionImagePath:\
\
string\
\
未发布作业指示图像路径\
\
unpublishedInstructionThumbnailPath:\
\
string\
\
未发布作业指示缩略图路径\
\
}\
\
\]\
\
}\
\
\]

}

}

* * *

# listJobProcesses

获取终端工作流程列表

获取终端工作流程列表

```
/api/terminal/job-processes
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-listJobProcesses-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/job-processes"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalCommonReqDTO body = ; // TerminalCommonReqDTO |
        try {
            ResultTerminalListJobProcessesRespDTO result = apiInstance.listJobProcesses(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#listJobProcesses");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalCommonReqDTO body = ; // TerminalCommonReqDTO |
        try {
            ResultTerminalListJobProcessesRespDTO result = apiInstance.listJobProcesses(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#listJobProcesses");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalCommonReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 获取终端工作流程列表
[apiInstance listJobProcessesWith:body\
              completionHandler: ^(ResultTerminalListJobProcessesRespDTO output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalCommonReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.listJobProcesses(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class listJobProcessesExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalCommonReqDTO(); // TerminalCommonReqDTO |

            try
            {
                // 获取终端工作流程列表
                ResultTerminalListJobProcessesRespDTO result = apiInstance.listJobProcesses(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.listJobProcesses: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalCommonReqDTO |

try {
    $result = $api_instance->listJobProcesses($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->listJobProcesses: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalCommonReqDTO->new(); # TerminalCommonReqDTO |

eval {
    my $result = $api_instance->listJobProcesses(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->listJobProcesses: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalCommonReqDTO |

try:
    # 获取终端工作流程列表
    api_response = api_instance.list_job_processes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->listJobProcesses: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端通用请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>} |

## Responses

### Status: 200 - 成功获取终端工作流程列表

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-listJobProcesses-200-schema)

{

code:

integer(int32)

message:

string

data:

{

获取终端工作流程列表

terminalCode:

string

终端编码

jobProcesses:

\[\
\
作业流程列表\
\
{\
\
作业流程\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
version:\
\
integer(int32)\
\
版本\
\
name:\
\
string\
\
作业流程名称\
\
deviceId:\
\
integer(int32)\
\
所属终端\
\
deviceUuid:\
\
string\
\
所属终端唯一标识\
\
autoLoop:\
\
integer(int32)\
\
是否自动循环（0: 否, 1: 是）\
\
ngTerminate:\
\
integer(int32)\
\
NG是否终止（0: 否, 1: 是）\
\
isDefault:\
\
integer(int32)\
\
是否默认作业流程（0: 否, 1: 是）\
\
isPublished:\
\
integer(int32)\
\
是否已发布（0: 否, 1: 是）\
\
creatorId:\
\
integer(int32)\
\
创建者ID\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
publishedAt:\
\
string(date-time)\
\
发布时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
deviceName:\
\
string\
\
终端名称\
\
terminalCode:\
\
string\
\
终端编码\
\
hardwareCode:\
\
string\
\
硬件编码\
\
jobInstructions:\
\
\[\
\
作业指示列表\
\
{\
\
作业指示\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
instructionText:\
\
string\
\
作业指示文本\
\
instructionImage:\
\
string\
\
作业指示图像（存储图像路径）\
\
instructionImageSize:\
\
integer(int64)\
\
图像大小（单位：字节）\
\
instructionImageChecksum:\
\
string\
\
图像校验值（如MD5）\
\
instructionThumbnail:\
\
string\
\
作业指示缩略图（存储缩略图路径）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
jobItems:\
\
\[\
\
作业项列表\
\
{\
\
作业项\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobInstructionId:\
\
integer(int32)\
\
所属作业指示\
\
jobInstructionUuid:\
\
string\
\
所属作业指示唯一标识\
\
itemImage:\
\
string\
\
作业项目图像\
\
itemImageSize:\
\
integer(int64)\
\
图像大小（单位：字节）\
\
itemImageChecksum:\
\
string\
\
图像校验值（如MD5）\
\
itemThumbnail:\
\
string\
\
作业项目缩略图\
\
mode:\
\
string\
\
模式（匹配模式，其他模式）\
\
standardTime:\
\
integer(int32)\
\
标准时间（单位：秒）\
\
upperLimitTime:\
\
integer(int32)\
\
上限时间（单位：秒）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
deviceScreenshotId:\
\
integer(int32)\
\
主图像Id\
\
baseSearchArea:\
\
{\
\
校验点\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobItemId:\
\
integer(int32)\
\
所属作业项目\
\
jobItemUuid:\
\
string\
\
所属作业项目唯一标识\
\
type:\
\
string\
\
类型：'BASE\_POINT', 'CHECK\_POINT', 'BASE\_SEARCH\_AREA'\
\
**Enum:** `BASE_POINT`, `CHECK_POINT`, `BASE_SEARCH_AREA`\
\
shape:\
\
string\
\
形状：'RECTANGLE', 'POLYGON'\
\
**Enum:** `RECTANGLE`, `POLYGON`\
\
left:\
\
integer(int32)\
\
左上角x坐标\
\
top:\
\
integer(int32)\
\
左上角y坐标\
\
width:\
\
integer(int32)\
\
矩形框的宽度\
\
height:\
\
integer(int32)\
\
矩形框的高度\
\
snapshot:\
\
string\
\
截图\
\
snapshotSize:\
\
integer(int64)\
\
图片大小（单位：字节）\
\
snapshotChecksum:\
\
string\
\
图片校验值（如MD5）\
\
snapshotBase64:\
\
string\
\
截图Base64，只用于前端传入\
\
similarity:\
\
number(double)\
\
相似度（范围0.50-1.00）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
unpublishedSnapshotPath:\
\
string\
\
未发布截图路径\
\
}\
\
basePoint:\
\
{\
\
校验点\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobItemId:\
\
integer(int32)\
\
所属作业项目\
\
jobItemUuid:\
\
string\
\
所属作业项目唯一标识\
\
type:\
\
string\
\
类型：'BASE\_POINT', 'CHECK\_POINT', 'BASE\_SEARCH\_AREA'\
\
**Enum:** `BASE_POINT`, `CHECK_POINT`, `BASE_SEARCH_AREA`\
\
shape:\
\
string\
\
形状：'RECTANGLE', 'POLYGON'\
\
**Enum:** `RECTANGLE`, `POLYGON`\
\
left:\
\
integer(int32)\
\
左上角x坐标\
\
top:\
\
integer(int32)\
\
左上角y坐标\
\
width:\
\
integer(int32)\
\
矩形框的宽度\
\
height:\
\
integer(int32)\
\
矩形框的高度\
\
snapshot:\
\
string\
\
截图\
\
snapshotSize:\
\
integer(int64)\
\
图片大小（单位：字节）\
\
snapshotChecksum:\
\
string\
\
图片校验值（如MD5）\
\
snapshotBase64:\
\
string\
\
截图Base64，只用于前端传入\
\
similarity:\
\
number(double)\
\
相似度（范围0.50-1.00）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
unpublishedSnapshotPath:\
\
string\
\
未发布截图路径\
\
}\
\
checkPoints:\
\
\[\
\
校验点列表\
\
{\
\
校验点\
\
id:\
\
integer(int32)\
\
ID\
\
uuid:\
\
string\
\
唯一标识\
\
jobProcessId:\
\
integer(int32)\
\
所属作业流程\
\
jobProcessUuid:\
\
string\
\
所属作业流程唯一标识\
\
jobItemId:\
\
integer(int32)\
\
所属作业项目\
\
jobItemUuid:\
\
string\
\
所属作业项目唯一标识\
\
type:\
\
string\
\
类型：'BASE\_POINT', 'CHECK\_POINT', 'BASE\_SEARCH\_AREA'\
\
**Enum:** `BASE_POINT`, `CHECK_POINT`, `BASE_SEARCH_AREA`\
\
shape:\
\
string\
\
形状：'RECTANGLE', 'POLYGON'\
\
**Enum:** `RECTANGLE`, `POLYGON`\
\
left:\
\
integer(int32)\
\
左上角x坐标\
\
top:\
\
integer(int32)\
\
左上角y坐标\
\
width:\
\
integer(int32)\
\
矩形框的宽度\
\
height:\
\
integer(int32)\
\
矩形框的高度\
\
snapshot:\
\
string\
\
截图\
\
snapshotSize:\
\
integer(int64)\
\
图片大小（单位：字节）\
\
snapshotChecksum:\
\
string\
\
图片校验值（如MD5）\
\
snapshotBase64:\
\
string\
\
截图Base64，只用于前端传入\
\
similarity:\
\
number(double)\
\
相似度（范围0.50-1.00）\
\
stepOrder:\
\
integer(int32)\
\
步骤顺序\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
updatedAt:\
\
string(date-time)\
\
更新时间\
\
deleted:\
\
integer(int32)\
\
是否已删除（0: 否, 1: 是）\
\
unpublishedSnapshotPath:\
\
string\
\
未发布截图路径\
\
}\
\
\]\
\
unpublishedItemImagePath:\
\
string\
\
未发布作业项图像路径\
\
unpublishedItemThumbnailPath:\
\
string\
\
未发布作业项缩略图路径\
\
}\
\
\]\
\
unpublishedInstructionImagePath:\
\
string\
\
未发布作业指示图像路径\
\
unpublishedInstructionThumbnailPath:\
\
string\
\
未发布作业指示缩略图路径\
\
}\
\
\]\
\
}\
\
\]

}

}

* * *

# refresh

终端心跳消息上报

终端心跳消息上报

```
/api/terminal/refresh
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-refresh-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/refresh"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalRefreshReqDTO body = ; // TerminalRefreshReqDTO |
        try {
            ResultTerminalRefreshRespDTO result = apiInstance.refresh(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#refresh");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalRefreshReqDTO body = ; // TerminalRefreshReqDTO |
        try {
            ResultTerminalRefreshRespDTO result = apiInstance.refresh(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#refresh");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalRefreshReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端心跳消息上报
[apiInstance refreshWith:body\
              completionHandler: ^(ResultTerminalRefreshRespDTO output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalRefreshReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.refresh(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class refreshExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalRefreshReqDTO(); // TerminalRefreshReqDTO |

            try
            {
                // 终端心跳消息上报
                ResultTerminalRefreshRespDTO result = apiInstance.refresh(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.refresh: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalRefreshReqDTO |

try {
    $result = $api_instance->refresh($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->refresh: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalRefreshReqDTO->new(); # TerminalRefreshReqDTO |

eval {
    my $result = $api_instance->refresh(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->refresh: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalRefreshReqDTO |

try:
    # 终端心跳消息上报
    api_response = api_instance.refresh(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->refresh: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端心跳消息上报请求参数<br>Required: hardwareCode,terminalCode,workStatus<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>workStatus:<br>string<br>工作状态（IDLE 待机，WORKING 工作）<br>timestamp:<br>integer(int64)<br>时间戳<br>} |

## Responses

### Status: 200 - 成功上报终端心跳消息

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-refresh-200-schema)

{

code:

integer(int32)

message:

string

data:

{

终端刷新响应参数

terminalCode:

string

终端编码

timestamp:

integer(int64)

时间戳

appVersion:

{

APP版本

id:

integer

versionName:

string

versionNumber:

integer

file:

string

fileName:

string

fileSize:

integer

checksum:

string

createdAt:

string

updatedAt:

string

}

notifications:

\[\
\
终端通知消息列表\
\
{\
\
终端通知实体\
\
id:\
\
integer(int32)\
\
通知ID\
\
type:\
\
string\
\
指令类型\
\
**Enum:** `CONFIG`, `SCHEDULE`, `JOB_PROCESS`, `SCREENSHOT`, `REBOOT`, `POWER_OFF`, `LOG_UPLOAD`\
\
parameters:\
\
string\
\
指令参数（可以是 JSON 字符串）\
\
deviceId:\
\
integer(int32)\
\
关联的终端 ID\
\
status:\
\
string\
\
状态（UNSENT: 未分发，SENT: 已分发）\
\
**Enum:** `UNSENT`, `SENT`\
\
createdAt:\
\
string(date-time)\
\
创建时间\
\
dispatchedAt:\
\
string(date-time)\
\
分发时间\
\
}\
\
\]

}

}

* * *

# reportCrash

终端上报崩溃日志(旧)

终端上报崩溃日志接口(旧)

```
/api/terminal/report_crash
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/report_crash"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        String body = ; // String |
        try {
            ResultVoid result = apiInstance.reportCrash(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportCrash");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        String body = ; // String |
        try {
            ResultVoid result = apiInstance.reportCrash(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportCrash");
            e.printStackTrace();
        }
    }
}
```

```cpp
String *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端上报崩溃日志(旧)
[apiInstance reportCrashWith:body\
              completionHandler: ^(ResultVoid output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{String}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.reportCrash(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class reportCrashExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new String(); // String |

            try
            {
                // 终端上报崩溃日志(旧)
                ResultVoid result = apiInstance.reportCrash(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.reportCrash: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // String |

try {
    $result = $api_instance->reportCrash($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->reportCrash: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::String->new(); # String |

eval {
    my $result = $api_instance->reportCrash(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->reportCrash: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # String |

try:
    # 终端上报崩溃日志(旧)
    api_response = api_instance.report_crash(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->reportCrash: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | string<br>终端上报崩溃日志请求参数 |

## Responses

### Status: 200 - 成功上报崩溃日志(旧)

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-reportCrash-200-schema)

{

code:

integer(int32)

message:

string

data:

{

}

}

* * *

# reportCrash1

终端上报崩溃日志

终端上报崩溃日志接口

```
/api/terminal/report-crash
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportCrash1-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/report-crash"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportCrashReqDTO body = ; // TerminalReportCrashReqDTO |
        try {
            ResultVoid result = apiInstance.reportCrash1(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportCrash1");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportCrashReqDTO body = ; // TerminalReportCrashReqDTO |
        try {
            ResultVoid result = apiInstance.reportCrash1(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportCrash1");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalReportCrashReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端上报崩溃日志
[apiInstance reportCrash1With:body\
              completionHandler: ^(ResultVoid output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalReportCrashReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.reportCrash1(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class reportCrash1Example
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalReportCrashReqDTO(); // TerminalReportCrashReqDTO |

            try
            {
                // 终端上报崩溃日志
                ResultVoid result = apiInstance.reportCrash1(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.reportCrash1: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalReportCrashReqDTO |

try {
    $result = $api_instance->reportCrash1($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->reportCrash1: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalReportCrashReqDTO->new(); # TerminalReportCrashReqDTO |

eval {
    my $result = $api_instance->reportCrash1(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->reportCrash1: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalReportCrashReqDTO |

try:
    # 终端上报崩溃日志
    api_response = api_instance.report_crash1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->reportCrash1: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端上报崩溃日志请求参数<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>ipAddress:<br>string<br>IP 地址<br>macAddress:<br>string<br>MAC 地址<br>versionName:<br>string<br>版本名称<br>versionNumber:<br>string<br>版本号<br>stack:<br>string<br>崩溃堆栈<br>other:<br>string<br>其他信息<br>} |

## Responses

### Status: 200 - 成功上报崩溃日志

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-reportCrash1-200-schema)

{

code:

integer(int32)

message:

string

data:

{

}

}

* * *

# reportJobItemLog

终端上报作业项目日志

终端上报作业项目日志

```
/api/terminal/report-job-item-log
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemLog-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/report-job-item-log"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportJobItemLogReqDTO body = ; // TerminalReportJobItemLogReqDTO |
        try {
            ResultVoid result = apiInstance.reportJobItemLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportJobItemLog");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportJobItemLogReqDTO body = ; // TerminalReportJobItemLogReqDTO |
        try {
            ResultVoid result = apiInstance.reportJobItemLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportJobItemLog");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalReportJobItemLogReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端上报作业项目日志
[apiInstance reportJobItemLogWith:body\
              completionHandler: ^(ResultVoid output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalReportJobItemLogReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.reportJobItemLog(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class reportJobItemLogExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalReportJobItemLogReqDTO(); // TerminalReportJobItemLogReqDTO |

            try
            {
                // 终端上报作业项目日志
                ResultVoid result = apiInstance.reportJobItemLog(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.reportJobItemLog: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalReportJobItemLogReqDTO |

try {
    $result = $api_instance->reportJobItemLog($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->reportJobItemLog: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalReportJobItemLogReqDTO->new(); # TerminalReportJobItemLogReqDTO |

eval {
    my $result = $api_instance->reportJobItemLog(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->reportJobItemLog: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalReportJobItemLogReqDTO |

try:
    # 终端上报作业项目日志
    api_response = api_instance.report_job_item_log(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->reportJobItemLog: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端上报作业项目日志请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>uuid:<br>string<br>唯一标识<br>jobProcessLogUuid:<br>string<br>所属作业流程日志<br>jobItemId:<br>integer(int32)<br>所属作业项目<br>status:<br>string<br>作业项目状态（PROCESSING: 进行中，COMPLETED: 完成，FAILED: 失败，CANCELLED: 取消）<br>**Enum:** `PROCESSING`, `COMPLETED`, `FAILED`, `CANCELLED`<br>startTime:<br>integer(int64)<br>开始时间，单位：毫秒<br>endTime:<br>integer(int64)<br>结束时间，单位：毫秒<br>jobItemTimeout:<br>integer(int32)<br>是否超时（0: 否, 1: 是）<br>} |

## Responses

### Status: 200 - 成功上报作业项目日志

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-reportJobItemLog-200-schema)

{

code:

integer(int32)

message:

string

data:

{

}

}

* * *

# reportJobItemPointLog

终端上报作业项目校验点日志

终端上报作业项目校验点日志

```
/api/terminal/report-job-item-point-log
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobItemPointLog-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/report-job-item-point-log"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportJobItemPointLogReqDTO body = ; // TerminalReportJobItemPointLogReqDTO |
        try {
            ResultVoid result = apiInstance.reportJobItemPointLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportJobItemPointLog");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportJobItemPointLogReqDTO body = ; // TerminalReportJobItemPointLogReqDTO |
        try {
            ResultVoid result = apiInstance.reportJobItemPointLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportJobItemPointLog");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalReportJobItemPointLogReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端上报作业项目校验点日志
[apiInstance reportJobItemPointLogWith:body\
              completionHandler: ^(ResultVoid output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalReportJobItemPointLogReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.reportJobItemPointLog(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class reportJobItemPointLogExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalReportJobItemPointLogReqDTO(); // TerminalReportJobItemPointLogReqDTO |

            try
            {
                // 终端上报作业项目校验点日志
                ResultVoid result = apiInstance.reportJobItemPointLog(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.reportJobItemPointLog: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalReportJobItemPointLogReqDTO |

try {
    $result = $api_instance->reportJobItemPointLog($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->reportJobItemPointLog: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalReportJobItemPointLogReqDTO->new(); # TerminalReportJobItemPointLogReqDTO |

eval {
    my $result = $api_instance->reportJobItemPointLog(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->reportJobItemPointLog: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalReportJobItemPointLogReqDTO |

try:
    # 终端上报作业项目校验点日志
    api_response = api_instance.report_job_item_point_log(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->reportJobItemPointLog: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端上报作业项目校验点日志请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>uuid:<br>string<br>唯一标识<br>jobProcessLogUuid:<br>string<br>所属作业流程日志<br>jobItemLogUuid:<br>string<br>所属作业项目日志<br>jobItemPointId:<br>integer(int32)<br>所属作业项目校验点<br>status:<br>string<br>作业项目校验点状态（PROCESSING: 进行中，COMPLETED: 完成，FAILED: 失败，CANCELLED: 取消）<br>**Enum:** `PROCESSING`, `COMPLETED`, `FAILED`, `CANCELLED`<br>startTime:<br>integer(int64)<br>开始时间，单位：毫秒<br>endTime:<br>integer(int64)<br>结束时间，单位：毫秒<br>errorCode:<br>string<br>错误码<br>description:<br>string<br>描述<br>similarity:<br>number(double)<br>相似度<br>snapshotBase64:<br>string<br>校验点截图<br>} |

## Responses

### Status: 200 - 成功上报作业项目校验点日志

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-reportJobItemPointLog-200-schema)

{

code:

integer(int32)

message:

string

data:

{

}

}

* * *

# reportJobProcessLog

终端上报作业流程日志

终端上报作业流程日志

```
/api/terminal/report-job-process-log
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-reportJobProcessLog-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/report-job-process-log"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportJobProcessLogReqDTO body = ; // TerminalReportJobProcessLogReqDTO |
        try {
            ResultVoid result = apiInstance.reportJobProcessLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportJobProcessLog");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        TerminalReportJobProcessLogReqDTO body = ; // TerminalReportJobProcessLogReqDTO |
        try {
            ResultVoid result = apiInstance.reportJobProcessLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#reportJobProcessLog");
            e.printStackTrace();
        }
    }
}
```

```cpp
TerminalReportJobProcessLogReqDTO *body = ; //

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端上报作业流程日志
[apiInstance reportJobProcessLogWith:body\
              completionHandler: ^(ResultVoid output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var body = ; // {{TerminalReportJobProcessLogReqDTO}}

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.reportJobProcessLog(body, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class reportJobProcessLogExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new TerminalReportJobProcessLogReqDTO(); // TerminalReportJobProcessLogReqDTO |

            try
            {
                // 终端上报作业流程日志
                ResultVoid result = apiInstance.reportJobProcessLog(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.reportJobProcessLog: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // TerminalReportJobProcessLogReqDTO |

try {
    $result = $api_instance->reportJobProcessLog($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->reportJobProcessLog: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::TerminalReportJobProcessLogReqDTO->new(); # TerminalReportJobProcessLogReqDTO |

eval {
    my $result = $api_instance->reportJobProcessLog(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->reportJobProcessLog: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # TerminalReportJobProcessLogReqDTO |

try:
    # 终端上报作业流程日志
    api_response = api_instance.report_job_process_log(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->reportJobProcessLog: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body \* | {<br>终端上报作业流程日志请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>硬件编码<br>terminalCode:<br>string<br>终端编码<br>uuid:<br>string<br>作业流程日志唯一标识<br>jobProcessId:<br>integer(int32)<br>所属作业流程ID<br>version:<br>integer(int32)<br>作业流程版本<br>status:<br>string<br>作业流程状态（PROCESSING: 进行中，COMPLETED: 完成，FAILED: 失败，CANCELLED: 取消）<br>**Enum:** `PROCESSING`, `COMPLETED`, `FAILED`, `CANCELLED`<br>startTime:<br>integer(int64)<br>开始时间，单位：毫秒<br>endTime:<br>integer(int64)<br>结束时间，单位：毫秒<br>} |

## Responses

### Status: 200 - 成功上报作业流程日志

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-reportJobProcessLog-200-schema)

{

code:

integer(int32)

message:

string

data:

{

}

}

* * *

# uploadDeviceLog

终端上报设备日志

终端上报设备日志接口

```
/api/terminal/upload-device-log
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadDeviceLog-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/upload-device-log"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        Terminal_uploaddevicelog_body body = ; // Terminal_uploaddevicelog_body |
        try {
            ResultVoid result = apiInstance.uploadDeviceLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#uploadDeviceLog");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        Terminal_uploaddevicelog_body body = ; // Terminal_uploaddevicelog_body |
        try {
            ResultVoid result = apiInstance.uploadDeviceLog(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#uploadDeviceLog");
            e.printStackTrace();
        }
    }
}
```

```cpp
Terminal_uploaddevicelog_body *body = ; //  (optional)

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端上报设备日志
[apiInstance uploadDeviceLogWith:body\
              completionHandler: ^(ResultVoid output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var opts = {
  'body':  // {{Terminal_uploaddevicelog_body}}
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.uploadDeviceLog(opts, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class uploadDeviceLogExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new Terminal_uploaddevicelog_body(); // Terminal_uploaddevicelog_body |  (optional)

            try
            {
                // 终端上报设备日志
                ResultVoid result = apiInstance.uploadDeviceLog(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.uploadDeviceLog: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // Terminal_uploaddevicelog_body |

try {
    $result = $api_instance->uploadDeviceLog($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->uploadDeviceLog: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::Terminal_uploaddevicelog_body->new(); # Terminal_uploaddevicelog_body |

eval {
    my $result = $api_instance->uploadDeviceLog(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->uploadDeviceLog: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # Terminal_uploaddevicelog_body |  (optional)

try:
    # 终端上报设备日志
    api_response = api_instance.upload_device_log(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->uploadDeviceLog: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body | {<br>Required: file,meta<br>meta:<br>{<br>终端通用请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>terminalCode:<br>string<br>}<br>file:<br>string(binary)<br>设备日志文件<br>} |

## Responses

### Status: 200 - 成功上报设备日志

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-uploadDeviceLog-200-schema)

{

code:

integer(int32)

message:

string

data:

{

}

}

* * *

# uploadScreenshot

终端上报截图

终端上报截图接口

```
/api/terminal/upload-screenshot
```

### Usage and SDK Samples

- [Curl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-curl)
- [Java](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-java)
- [Android](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-android)
- [Obj-C](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-objc)
- [JavaScript](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-javascript)
- [C#](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-csharp)
- [PHP](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-php)
- [Perl](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-perl)
- [Python](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#examples-TerminalController-uploadScreenshot-0-python)

```bsh
curl -X POST\
-H "Accept: */*"\
-H "Content-Type: application/json"\
"http://localhost:8020/api/terminal/upload-screenshot"
```

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.TerminalControllerApi;

import java.io.File;
import java.util.*;

public class TerminalControllerApiExample {

    public static void main(String[] args) {

        TerminalControllerApi apiInstance = new TerminalControllerApi();
        Terminal_uploadscreenshot_body body = ; // Terminal_uploadscreenshot_body |
        try {
            ResultVoid result = apiInstance.uploadScreenshot(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#uploadScreenshot");
            e.printStackTrace();
        }
    }
}
```

```java
import io.swagger.client.api.TerminalControllerApi;

public class TerminalControllerApiExample {

    public static void main(String[] args) {
        TerminalControllerApi apiInstance = new TerminalControllerApi();
        Terminal_uploadscreenshot_body body = ; // Terminal_uploadscreenshot_body |
        try {
            ResultVoid result = apiInstance.uploadScreenshot(body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TerminalControllerApi#uploadScreenshot");
            e.printStackTrace();
        }
    }
}
```

```cpp
Terminal_uploadscreenshot_body *body = ; //  (optional)

TerminalControllerApi *apiInstance = [[TerminalControllerApi alloc] init];

// 终端上报截图
[apiInstance uploadScreenshotWith:body\
              completionHandler: ^(ResultVoid output, NSError* error) {\
                            if (output) {\
                                NSLog(@"%@", output);\
                            }\
                            if (error) {\
                                NSLog(@"Error: %@", error);\
                            }\
                        }];
```

```js
var Api = require('_api');

var api = new Api.TerminalControllerApi()
var opts = {
  'body':  // {{Terminal_uploadscreenshot_body}}
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.uploadScreenshot(opts, callback);
```

```cs
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class uploadScreenshotExample
    {
        public void main()
        {

            var apiInstance = new TerminalControllerApi();
            var body = new Terminal_uploadscreenshot_body(); // Terminal_uploadscreenshot_body |  (optional)

            try
            {
                // 终端上报截图
                ResultVoid result = apiInstance.uploadScreenshot(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TerminalControllerApi.uploadScreenshot: " + e.Message );
            }
        }
    }
}
```

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\ApiTerminalControllerApi();
$body = ; // Terminal_uploadscreenshot_body |

try {
    $result = $api_instance->uploadScreenshot($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TerminalControllerApi->uploadScreenshot: ', $e->getMessage(), PHP_EOL;
}
?>
```

```perl
use Data::Dumper;
use WWW::SwaggerClient::Configuration;
use WWW::SwaggerClient::TerminalControllerApi;

my $api_instance = WWW::SwaggerClient::TerminalControllerApi->new();
my $body = WWW::SwaggerClient::Object::Terminal_uploadscreenshot_body->new(); # Terminal_uploadscreenshot_body |

eval {
    my $result = $api_instance->uploadScreenshot(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling TerminalControllerApi->uploadScreenshot: $@\n";
}
```

```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalControllerApi()
body =  # Terminal_uploadscreenshot_body |  (optional)

try:
    # 终端上报截图
    api_response = api_instance.upload_screenshot(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalControllerApi->uploadScreenshot: %s\n" % e)
```

## Parameters

Body parameters

| Name | Description |
| --- | --- |
| body | {<br>Required: file,meta<br>meta:<br>{<br>终端通用请求参数<br>Required: hardwareCode,terminalCode<br>hardwareCode:<br>string<br>terminalCode:<br>string<br>}<br>file:<br>string(binary)<br>截图文件<br>} |

## Responses

### Status: 200 - 成功上报截图

- [Schema](https://pixsign.apexvuedigital.com/pixdata/wukong-api-doc/#responses-uploadScreenshot-200-schema)

{

code:

integer(int32)

message:

string

data:

{

}

}

* * *