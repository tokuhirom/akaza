#ifndef LIBAKAZA_AKAZA_H_
#define LIBAKAZA_AKAZA_H_

#include "binary_dict.h"
#include "system_lm.h"
#include "tinylisp.h"
#include "user_language_model.h"
#include "node.h"
#include "graph.h"
#include "graph_resolver.h"
#include "romkan.h"

namespace akaza {
    class Akaza {
    private:
        std::shared_ptr<GraphResolver> graphResolver_;
        std::shared_ptr<RomkanConverter> romkanConverter_;
    public:
        Akaza(std::shared_ptr<GraphResolver> &graphResolver, std::shared_ptr<RomkanConverter> &romkanConverter) {
            graphResolver_ = graphResolver;
            romkanConverter_ = romkanConverter;
        }

        std::vector<std::vector<std::shared_ptr<Node>>> convert(
                const std::wstring &s,
                const std::optional<std::vector<Slice>> &forceSelectedClauses);

        std::string get_version();
    };
}

#endif // LIBAKAZA_AKAZA_H_
