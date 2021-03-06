cmake_minimum_required(VERSION 3.17)
project(libakaza)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 17)
SET(CMAKE_C_FLAGS "-Wall -O2 -g ${CC_WARNING_FLAGS} ${CMAKE_C_FLAGS}")

# =============================================================================================
#
# library
#
# =============================================================================================

add_library(akaza SHARED include/tinylisp.h src/tinylisp.cc src/binary_dict.cc include/user_language_model.h
        src/user_language_model.cc src/split.h include/node.h src/node.cc include/graph.h include/graph_resolver.h
        src/graph_resolver.cc src/graph.cc src/debug_log.h include/romkan.h src/romkan.cc src/romkan_default.h
        src/akaza.cc src/system_lm.cc src/kana.cc)
target_link_libraries(akaza marisa)

install(TARGETS akaza
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
file(GLOB HEADERS include/*.h)
install(FILES ${HEADERS} DESTINATION include/akaza/)

# =============================================================================================
#
# bin
#
# =============================================================================================
add_executable(akaza-make-system-lm bin/akaza-make-system-lm.cc)
target_link_libraries(akaza-make-system-lm marisa akaza)
install(TARGETS akaza-make-system-lm DESTINATION bin/)
set_target_properties(akaza-make-system-lm PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin/")

add_executable(akaza-make-binary-dict bin/akaza-make-binary-dict.cc)
target_link_libraries(akaza-make-binary-dict marisa akaza)
install(TARGETS akaza-make-binary-dict DESTINATION bin/)
set_target_properties(akaza-make-binary-dict PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin/")

add_executable(akaza-dump-systemlm-unigram bin/akaza-dump-systemlm-unigram.cc)
target_link_libraries(akaza-dump-systemlm-unigram marisa akaza)
install(TARGETS akaza-dump-systemlm-unigram DESTINATION bin/)
set_target_properties(akaza-dump-systemlm-unigram PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin/")

add_executable(akaza-benchmark bin/akaza-benchmark.cc)
target_link_libraries(akaza-benchmark marisa akaza)
install(TARGETS akaza-benchmark DESTINATION bin/)
set_target_properties(akaza-benchmark PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin/")

add_executable(binakaza bin/akaza.cc)
target_link_libraries(binakaza marisa akaza)
install(TARGETS binakaza DESTINATION bin/)
set_target_properties(binakaza PROPERTIES OUTPUT_NAME "akaza")
set_target_properties(binakaza PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin/")

# =============================================================================================
#
# pkg-config
#
# =============================================================================================

configure_file(akaza.pc.in akaza.pc @ONLY)
install(FILES ${CMAKE_BINARY_DIR}/akaza.pc DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)

# =============================================================================================
#
# test
#
# =============================================================================================

add_executable(00_systemlm.t t/00_systemlm.cc)
set_target_properties(00_systemlm.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(00_systemlm.t marisa akaza)
SET(TEST_EXES 00_systemlm.t)

add_executable(01_binary_dict.t t/01_binary_dict.cc)
set_target_properties(01_binary_dict.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(01_binary_dict.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 01_binary_dict.t)

add_executable(02_skk_dict.t t/02_skk_dict.cc)
set_target_properties(02_skk_dict.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(02_skk_dict.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 02_skk_dict.t)

add_executable(03_tinylisp.t t/03_tinylisp.cc)
set_target_properties(03_tinylisp.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(03_tinylisp.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 03_tinylisp.t)

add_executable(04_user_language_model.t t/04_user_language_model.cc)
set_target_properties(04_user_language_model.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(04_user_language_model.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 04_user_language_model.t)

add_executable(05_node.t t/05_node.cc)
set_target_properties(05_node.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(05_node.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 05_node.t)

add_executable(06_graph_resolver.t t/06_graph_resolver.cc)
set_target_properties(06_graph_resolver.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(06_graph_resolver.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 06_graph_resolver.t)

add_executable(07_romkan.t t/07_romkan.cc)
set_target_properties(07_romkan.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(07_romkan.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 07_romkan.t)

add_executable(08_akaza.t t/08_akaza.cc)
set_target_properties(08_akaza.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(08_akaza.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 08_akaza.t)

add_executable(10_integration.t t/10_integration.cc)
set_target_properties(10_integration.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(10_integration.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 10_integration.t)

add_executable(11_wnn.t t/11_wnn.cc)
set_target_properties(11_wnn.t PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/t/")
target_link_libraries(11_wnn.t marisa akaza)
SET(TEST_EXES ${TEST_EXES} 11_wnn.t)


ADD_CUSTOM_TARGET(test env BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR} prove --exec '' -v t/*.t
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} DEPENDS ${TEST_EXES})
