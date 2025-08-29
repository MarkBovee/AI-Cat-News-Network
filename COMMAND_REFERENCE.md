# AI Cat News Network - Command Line Reference

## Quick Commands for Automation

### Basic Usage
```powershell
# Interactive mode (original behavior)
.\AI-Cat-News-Studio.ps1

# Direct commands (no waiting for prompts)
.\AI-Cat-News-Studio.ps1 1    # Generate script
.\AI-Cat-News-Studio.ps1 2    # Generate voice
.\AI-Cat-News-Studio.ps1 3    # Generate video metadata
.\AI-Cat-News-Studio.ps1 4    # Browse content
```

### Content Management
```powershell
# Clean old files only
.\AI-Cat-News-Studio.ps1 -clean

# Run command then clean
.\AI-Cat-News-Studio.ps1 2 -clean    # Voice + clean
.\AI-Cat-News-Studio.ps1 3 -clean    # Video + clean
```

### Help & Documentation
```powershell
# Show help
.\AI-Cat-News-Studio.ps1 -help
```

## Clean Functionality
- Keeps the **latest 3 files** in each content category
- Removes older files automatically
- Cleans: audio/, video/, scripts/, newsitems/, ideas/ directories
- Safe operation - preserves recent work

## Automation Examples

### Full Pipeline with Cleanup
```powershell
# Generate script
.\AI-Cat-News-Studio.ps1 1

# Generate voice with cleanup
.\AI-Cat-News-Studio.ps1 2 -clean

# Generate video metadata with cleanup  
.\AI-Cat-News-Studio.ps1 3 -clean

# Check final result
.\AI-Cat-News-Studio.ps1 4
```

### Quick Testing
```powershell
# Instant content browser (no prompts)
.\AI-Cat-News-Studio.ps1 4

# Generate voice and immediately check
.\AI-Cat-News-Studio.ps1 2
.\AI-Cat-News-Studio.ps1 4
```

### Maintenance
```powershell
# Clean up old files weekly
.\AI-Cat-News-Studio.ps1 -clean

# Reset content and start fresh
.\AI-Cat-News-Studio.ps1 -clean
.\AI-Cat-News-Studio.ps1 1
```

## Benefits
- **No waiting**: Direct execution without prompts
- **Automated cleanup**: Maintains organized content directory
- **Script-friendly**: Perfect for CI/CD and automated testing
- **Backwards compatible**: Original interactive mode still works
