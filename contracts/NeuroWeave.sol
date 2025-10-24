// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NeuroWeaveNFT is ERC721URIStorage, Ownable {
    uint256 public nextTokenId;

    constructor() ERC721("NeuroWeave CoCreation", "NWEAVE") Ownable(msg.sender) {}

    function safeMint(address to, string memory tokenUri) external onlyOwner {
        uint256 tokenId = nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenUri);
    }

    function _baseURI() internal pure override returns (string memory) {
        return "ipfs://";
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override  // Fixed: No explicit parent list
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}