{
    "targets": [
        {
            "target_name": "addon-ed25519",
            "sources": ["addon.cpp"],
      		"libraries": [ "<(module_root_dir)/../../target/release/libfrost_ed25519.so" ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
            ],
            "cflags!": ["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],
      		"defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
			"dependencies": [
				"<!(node -p \"require('node-addon-api').gyp\")"
			]
        },
        {
            "target_name": "addon-secp256k1",
            "sources": ["addon.cpp"],
      		"libraries": [ "<(module_root_dir)/../../target/release/libfrost_secp256k1.so" ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
            ],
            "cflags!": ["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],
      		"defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
			"dependencies": [
				"<!(node -p \"require('node-addon-api').gyp\")"
			]
        }
    ]
}
