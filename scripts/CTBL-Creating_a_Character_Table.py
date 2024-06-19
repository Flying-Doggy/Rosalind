# Creating a Character Table

import collections

class phylo_node:
    def __init__(self , val:str , n_type:str = None , sons:list = [] , parent = "None" ) -> None:
        self.val = val
        self.type = n_type
        self.s = sons
        self.p = parent
        pass

    def get_offsprings( self ):
        if self.type == 'leaf':
            return [self.val]
        else:
            tmp_res = [ ]
            for tmp_son in self.s:
                tmp_res.extend( tmp_son.get_offsprings() )
            return tmp_res
    
    def __repr__(self) -> str:
        return 'self:%s , parent:%s , sons:'%( self.val, self.p.val ) + str([son.val for son in self.s ])

def parse_nwk( nwk_s:str ) -> dict:
    phylo_dic = collections.defaultdict( phylo_node )
    internode_cnt = 0
    stack = [ '' ]
    idx = 0
    while idx < len(nwk_s):
        if nwk_s[idx] == ',' or nwk_s[idx] == ';' :
            stack.append( '' )
        elif nwk_s[idx]  == '(':
            stack[-1] += nwk_s[idx] 
            stack.append( '' )
        elif nwk_s[idx]  == ')':
            tmp_id = ''
            while nwk_s[idx+1] != ',' and nwk_s[idx+1] != ';' and nwk_s[idx+1] != ')':
                idx += 1
                tmp_id += nwk_s[idx]

            if tmp_id == '':
                tmp_id = internode_cnt
                internode_cnt += 1
            tmp_node = phylo_node( val=tmp_id, n_type='inter' , sons=[] )
            phylo_dic[tmp_id] = tmp_node

            tmp_sons = []
            while stack[-1] != '(':
                a = stack.pop()
                if a != '':
                    tmp_sons.append( a ) 
            stack.pop()
            stack.append( tmp_node )

            for son in tmp_sons:
                son_node = son
                if type(son) == str:
                    son_node = phylo_node( val=son , n_type='leaf' , parent=tmp_node)
                    phylo_dic[son] = son_node
                tmp_node.s.append( son_node )
                son_node.p = tmp_node
        else:
            stack[-1] += nwk_s[idx] 
        idx += 1
    
    return phylo_dic

a = parse_nwk('((((((((((((((((((((Acanthosaura_leucomystax,Paraphysa_eremita),(Apalone_mlokosiewiczi,(Odonthurus_franckii,Sphenurus_onocrotalus))),((Apus_meles,Spalax_leucopsis),Canis_torquatus)),Damon_cyanogaster),Querquedula_collectivus),Remiz_albirostris),Polypedates_taezanowskyi),(Equus_casualis,Xenophrys_caryocatactes)),(Dipsosaurus_argali,Nhandu_ibera)),Lampropeltis_bewickii),Almo_zenobia),((Hemitheconyx_weberi,(((Kassina_keyzerlingii,Motacilla_semipalmatus),Ninox_avosetta),Syrrhaptes_meles)),Lyrurus_weberi)),Porzana_turneri),(Cottus_leucostomum,Tadorna_capra)),(Nucifraga_trianguligerus,Ortigometra_maldivarum)),(Larus_geniculata,Rhynchaspis_citrsola)),(((((Alectoris_alterna,Antilope_vereda),((((((((((((((((((Aplopeltura_dulkeitiana,Machetes_cristatellus),Ursus_noctua),Pagophila_giganteus),(Canis_peregrinus,Tetrao_teguixin)),(Laudakia_scabra,Spizaetus_iguana)),Ceratophrys_acuta),(((Apodora_coloratovillosum,Diomedea_keyzerlingii),(((Eurynorhynchus_mycterizans,Paramesotriton_completus),(Pandion_solitaria,Tropidurus_chrysaetus)),(Larus_sauritus,Vormela_ampullatus))),(Grammostola_gecko,Rufibrenta_cygnoides))),(((((Ctenotus_citreola,Syrrhaptes_saiga),((Hydrosaurus_gordoni,Mustela_aegagrus),(Ophisops_leucophyllata,Streptopelia_ferruginea))),Larus_alterna),Odobenus_barroni),(Phelsuma_corsac,Telescopus_calyptratus))),Hysterocrates_elegans),Casarca_smithii),Callipogon_aureola),(Aythya_linaria,Damon_floridana)),((Arenaria_marmorata,((Basiliscus_hispida,((Calotes_alcinous,Capeila_avocetta),((Chelus_vipio,(Dryobates_subcinctus,((Odonthurus_alpestris,Porzana_clericalis),Recurvirostra_calvus))),Remiz_breitensteini))),Branta_eburnea)),(((((Bombyx_terrestris,((((((((Burhinus_meermani,Xenochrophis_insularis),Felis_lehmanni),crecca_semipalmatus),(Onychodactylus_limosa,Philothamnus_chukar)),Pseudemys_nasuta),Capra_deminutus),(Citellus_armeniacus,Micropalama_jubata)),(((((((Crotaphytus_eburnea,Physignathus_maculata),Lycodon_pulchripes),Totanus_sphenocercus),Tadorna_fasciata),Pseudorca_horridum),Micropalama_cherrug),Mustela_bifasciatus))),(Pandion_zonata,Pogona_monilis)),Seokia_licin),(Budytes_hodgsoni,Pelodytes_africanus)),(Phalacrocorax_kingii,Uroplatus_carnifex)))),Gongylophis_tataricus),Citharacanthus_atrigularis),Leiolepis_stagnalis),Gonyosoma_clypeatus),(((((Athene_leporosum,Crotaphytus_helvetica),Odobenus_similis),(Brachypelma_bobac,Physignathus_battersbyi)),Pagophila_sibirica),Bradypodion_rudicolis))),(Scaphiopus_murinus,Uromastyx_meermani)),Chlamydosaurus_piceus),(Leiurus_chrysaetus,Physignathus_aureola))),Chelydra_sphenocercus),((((((((Anolis_terrestris,Desnana_agama),Chamaeleo_carolinensis),(Eubalaena_virgo,Rhynchaspis_davidiana)),Pusa_tolai),(Kassina_aeruginosus,Petrocincla_ciliatus)),Thymallus_scincoides),((((((Babycurus_cinclus,Thamnophis_atrigularis),Burhinus_pulchripes),Natriciteres_taeniura),Megophrys_barbata),Chondropython_atra),Gonyosoma_himalayensis)),Chondropython_piscator)),(((((((((((Aix_glutinosus,Tiliqua_pygargus),Lycodon_mehelyi),Anthropoidae_brongersmai),(((Apus_flavolineata,Net_pedo),Pyxicephalus_vittatus),Brachypelma_leucostomum)),(Anthropoides_flava,(Calotes_sauritus,Chamaeleo_licin))),((((((Alcedo_cynodon,Pseudemys_ceterus),(Chlamydotis_quinquestriatus,Dipus_onocrotalus)),((((Allobates_corone,((Boiga_keyzerlingii,Xenopeltis_margaritifera),Sphenurus_rosmarus)),(Cuon_scutulata,(Eryx_kurilensis,Rosalia_naumanni))),((Bombina_chamaeleontinus,(Corvus_pallidus,((Dendrelaphis_quinquestriatus,(Dryobates_kuhli,Larus_gigas)),Gonyosoma_madagascariensis))),Tamias_arenarius)),(Haliaetus_leiosoma,((Osteopilus_parvus,Pandinus_reinwardti),Tringa_trigonopodus)))),Uncia_monachus),Net_sauromates),Oxyura_kingii)),Turdus_fulva),Eulabeia_schneideri),Pica_trigonopodus),Capra_squaterola),Cervus_oxycephalum),Aix_hardwickii);')
col_dic = dict( )
for idx,val in enumerate(sorted([ i.val for i in a.values() if i.type=='leaf'] )):
    col_dic[val] = idx


for tmp_node in a.values():
    if tmp_node.type == 'leaf':
        continue
    else:
        sub_set = tmp_node.get_offsprings() 
        if len( sub_set ) <= len(col_dic)-2:
            tmp_res = [ '0' for i in col_dic ]
            for i in sub_set:
                tmp_res[ col_dic[i] ] = '1'
            print( ''.join(tmp_res) )