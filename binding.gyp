{
	"targets": [{
		"target_name": "protobuf",
		"sources": [ "protobuf.cpp" ],
		"conditions": [
			["OS == 'win'", {
				"libraries": [
					"-llibprotobuf.lib"
				],
				"include_dirs": [
					"$(LIBPROTOBUF)/include"
				],
				"msvs_settings": {
					"VCLinkerTool": {
						"AdditionalLibraryDirectories": "$(LIBPROTOBUF)/lib"
					}
				}
			}],
			["OS == 'mac'", {
                "libraries": [
                    "-lprotobuf"
                ],
                "xcode_settings": {
                    "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                    "OTHER_CFLAGS": [
                        "-g",
                        "-mmacosx-version-min=10.7",
                        "-std=c++11",
                        "-stdlib=libc++",
                        "-O3",
                        "-D__STDC_CONSTANT_MACROS",
                        "-D_FILE_OFFSET_BITS=64",
                        "-D_LARGEFILE_SOURCE",
                        "-Wall"
                    ],
                    "OTHER_CPLUSPLUSFLAGS": [
                        "-g",
                        "-mmacosx-version-min=10.7",
                        "-std=c++11",
                        "-stdlib=libc++",
                        "-O3",
                        "-D__STDC_CONSTANT_MACROS",
                        "-D_FILE_OFFSET_BITS=64",
                        "-D_LARGEFILE_SOURCE",
                        "-Wall"
                    ]
                }
            }],
			["OS == 'linux'", {
				"libraries": [
					"-lprotobuf"
				]
			}]
		]
	}]
}
