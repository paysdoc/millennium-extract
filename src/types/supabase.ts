
export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      character: {
        Row: {
          id: number
          name: string | null
          first_names: string | null
          birth_date: string | null
          death_date: string | null
          biography: string | null
          type: string | null
          link: string | null
          image_link: string | null
          joker_type: string | null
          joker_type_value: number | null
          joker_type_why: string | null
          joker_type_why_short: string | null
        }
        Insert: {
          id?: number
          name?: string | null
          first_names?: string | null
          birth_date?: string | null
          death_date?: string | null
          biography?: string | null
          type?: string | null
          link?: string | null
          image_link?: string | null
          joker_type?: string | null
          joker_type_value?: number | null
          joker_type_why?: string | null
          joker_type_why_short?: string | null
        }
        Update: {
          id?: number
          name?: string | null
          first_names?: string | null
          birth_date?: string | null
          death_date?: string | null
          biography?: string | null
          type?: string | null
          link?: string | null
          image_link?: string | null
          joker_type?: string | null
          joker_type_value?: number | null
          joker_type_why?: string | null
          joker_type_why_short?: string | null
        }
      }
      connection: {
        Row: {
          id: number
          char1_id: number | null
          char2_id: number | null
          value: number | null
          why: string | null
          active: boolean | null
        }
        Insert: {
          id?: number
          char1_id?: number | null
          char2_id?: number | null
          value?: number | null
          why?: string | null
          active?: boolean | null
        }
        Update: {
          id?: number
          char1_id?: number | null
          char2_id?: number | null
          value?: number | null
          why?: string | null
          active?: boolean | null
        }
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      [_ in never]: never
    }
    Enums: {
      [_ in never]: never
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}
