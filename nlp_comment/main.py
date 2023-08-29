import micropip
from pyodide.ffi import to_js 
import asyncio

print('test')

PACKAGES_PATH = "/static"
CUSTOM_BUILT_PKG_NAMES = list(map(lambda name: f"{PACKAGES_PATH}/{name}-cp310-cp310-emscripten_3_1_14_wasm32.whl", [
    "blis-0.7.8",
    "cymem-2.0.6",
    "murmurhash-1.0.7",
    "preshed-3.0.6",
    "srsly-2.4.3",
    "thinc-8.1.0",
    "spacy-3.4.0",
]))




async def main():
    await micropip.install(CUSTOM_BUILT_PKG_NAMES)  # type: ignore 
    import pandas
    import matplotlib
    import spacy

asyncio.ensure_future(main())





