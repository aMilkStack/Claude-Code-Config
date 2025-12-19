#!/usr/bin/env node
import { readFileSync } from 'fs';
import { join } from 'path';

interface HookInput {
    session_id: string;
    transcript_path: string;
    cwd: string;
    permission_mode: string;
    prompt: string;
}

interface PromptTriggers {
    keywords?: string[];
    intentPatterns?: string[];
}

interface SkillRule {
    type: 'guardrail' | 'domain';
    enforcement: 'block' | 'suggest' | 'warn';
    priority: 'critical' | 'high' | 'medium' | 'low';
    promptTriggers?: PromptTriggers;
}

interface SkillRules {
    version: string;
    skills: Record<string, SkillRule>;
}

interface MatchedSkill {
    name: string;
    matchType: 'keyword' | 'intent';
    config: SkillRule;
}

async function main() {
    try {
        // Read input from stdin
        const input = readFileSync(0, 'utf-8');
        const data: HookInput = JSON.parse(input);
        const prompt = data.prompt.toLowerCase();

        // Load skill rules - check project first, then global
        const projectDir = process.env.CLAUDE_PROJECT_DIR || data.cwd;
        const homeDir = process.env.HOME || process.env.USERPROFILE || '';

        let rules: SkillRules | null = null;

        // Try project-level skill-rules.json first
        const projectRulesPath = join(projectDir, '.claude', 'skills', 'skill-rules.json');
        try {
            rules = JSON.parse(readFileSync(projectRulesPath, 'utf-8'));
        } catch {
            // Try global skill-rules.json
            const globalRulesPath = join(homeDir, '.claude', 'skills', 'skill-rules.json');
            try {
                rules = JSON.parse(readFileSync(globalRulesPath, 'utf-8'));
            } catch {
                // No rules found, exit silently
                process.exit(0);
            }
        }

        if (!rules) {
            process.exit(0);
        }

        const matchedSkills: MatchedSkill[] = [];

        // Check each skill for matches
        for (const [skillName, config] of Object.entries(rules.skills)) {
            const triggers = config.promptTriggers;
            if (!triggers) {
                continue;
            }

            // Keyword matching
            if (triggers.keywords) {
                const keywordMatch = triggers.keywords.some(kw =>
                    prompt.includes(kw.toLowerCase())
                );
                if (keywordMatch) {
                    matchedSkills.push({ name: skillName, matchType: 'keyword', config });
                    continue;
                }
            }

            // Intent pattern matching
            if (triggers.intentPatterns) {
                const intentMatch = triggers.intentPatterns.some(pattern => {
                    const regex = new RegExp(pattern, 'i');
                    return regex.test(prompt);
                });
                if (intentMatch) {
                    matchedSkills.push({ name: skillName, matchType: 'intent', config });
                }
            }
        }

        // Generate output if matches found
        if (matchedSkills.length > 0) {
            // Separate SC commands, ultrathink, and regular skills
            const scCommands = matchedSkills.filter(s => s.name.startsWith('_sc:'));
            const ultrathink = matchedSkills.filter(s => s.name === '_ultrathink');
            const regularSkills = matchedSkills.filter(s => !s.name.startsWith('_'));

            let output = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n';
            output += '🎯 SMART SUGGESTIONS\n';
            output += '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n';

            // Ultrathink suggestion (critical priority)
            if (ultrathink.length > 0) {
                output += '🧠 DEEP THINKING RECOMMENDED:\n';
                output += '  → Type "ultrathink" for extended reasoning\n\n';
            }

            // SC Commands
            if (scCommands.length > 0) {
                output += '⚡ SC COMMANDS:\n';
                scCommands.forEach(s => {
                    const cmdName = s.name.replace('_', '');  // _sc:plan -> sc:plan
                    output += `  → /${cmdName}\n`;
                });
                output += '\n';
            }

            // Regular skills grouped by priority
            if (regularSkills.length > 0) {
                const critical = regularSkills.filter(s => s.config.priority === 'critical');
                const high = regularSkills.filter(s => s.config.priority === 'high');
                const medium = regularSkills.filter(s => s.config.priority === 'medium');
                const low = regularSkills.filter(s => s.config.priority === 'low');

                if (critical.length > 0) {
                    output += '⚠️ CRITICAL SKILLS:\n';
                    critical.forEach(s => output += `  → ${s.name}\n`);
                    output += '\n';
                }

                if (high.length > 0) {
                    output += '📚 RECOMMENDED SKILLS:\n';
                    high.forEach(s => output += `  → ${s.name}\n`);
                    output += '\n';
                }

                if (medium.length > 0) {
                    output += '💡 SUGGESTED SKILLS:\n';
                    medium.forEach(s => output += `  → ${s.name}\n`);
                    output += '\n';
                }

                if (low.length > 0) {
                    output += '📌 OPTIONAL SKILLS:\n';
                    low.forEach(s => output += `  → ${s.name}\n`);
                    output += '\n';
                }
            }

            output += '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n';

            console.log(output);
        }

        process.exit(0);
    } catch (err) {
        // Fail silently to not block prompts
        process.exit(0);
    }
}

main().catch(() => {
    process.exit(0);
});
